"""prepare_data.py -- 从 10x Genomics 原始数据生成教程所需的 npz 数据文件

本脚本仅供复现数据预处理流程、或将其迁移到你自己的 CITE-seq 数据。
运行教程 notebook 本身【不需要】执行本脚本(npz 文件已随教程提供)。

用法:
    python prepare_data.py            # 生成教程主数据 citeseq_pbmc.npz(PBMC 5k)
    python prepare_data.py pbmc10k    # 生成学生测试数据 citeseq_pbmc10k.npz(PBMC 10k)

数据来源(10x Genomics 公开数据,脚本会自动下载):
    pbmc5k : 5k PBMCs from a healthy donor, with cell surface proteins (v3, TotalSeq-B, 32 种蛋白)
    pbmc10k: 10k PBMCs from a healthy donor, with cell surface proteins (v3, TotalSeq-B, 17 种蛋白)

依赖(不在教程的 requirements.txt 中):scanpy
    pip install scanpy

输出(npz,约 1.4-1.8 MB),字段:
    X_rna      (n_cells, 1000) float32  RNA view:log 标准化后的 1000 个高变基因
    X_adt      (n_cells, p)    float32  ADT view:CLR 变换后的表面蛋白(去掉 IgG 对照)
    labels     (n_cells,)      str      参考细胞类型(由蛋白 marker 规则定义)
    adt_names  (p,)            str      ADT 特征名
    gene_names (1000,)         str      高变基因名
    lib_size   (n_cells,)      float32  每个细胞的总 UMI 数(QC 演示用)
    n_genes    (n_cells,)      float32  每个细胞检出的基因数(QC 演示用)
"""

import os
import sys
import urllib.request

import numpy as np
import scanpy as sc

DATASETS = {
    "pbmc5k": {
        "url": ("https://cf.10xgenomics.com/samples/cell-exp/3.0.2/"
                "5k_pbmc_protein_v3/5k_pbmc_protein_v3_filtered_feature_bc_matrix.h5"),
        "h5": "5k_pbmc_protein_v3_filtered_feature_bc_matrix.h5",
        "out": "citeseq_pbmc.npz",
        "markers": {"B cell": ["CD19", "CD20"], "Mono": ["CD14", "CD11b"],
                    "NK": ["CD56", "CD335"], "CD4 T": ["CD3", "CD4"], "CD8 T": ["CD3", "CD8a"]},
    },
    "pbmc10k": {
        "url": ("https://cf.10xgenomics.com/samples/cell-exp/3.0.0/"
                "pbmc_10k_protein_v3/pbmc_10k_protein_v3_filtered_feature_bc_matrix.h5"),
        "h5": "pbmc_10k_protein_v3_filtered_feature_bc_matrix.h5",
        "out": "citeseq_pbmc10k.npz",
        # pbmc10k 的 panel 没有 CD20/CD11b/CD335,使用替代 marker
        "markers": {"B cell": ["CD19"], "Mono": ["CD14", "CD15"],
                    "NK": ["CD56", "CD16"], "CD4 T": ["CD3", "CD4"], "CD8 T": ["CD3", "CD8a"]},
    },
}

sc.settings.verbosity = 0


def download_if_needed(cfg):
    if not os.path.exists(cfg["h5"]):
        print(f"downloading {cfg['url']} ...")
        # 10x 的服务器会拒绝 urllib 默认 UA,伪装成浏览器
        req = urllib.request.Request(cfg["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as r, open(cfg["h5"], "wb") as f:
            f.write(r.read())


def make_labels(X_adt, markers, marker_sets):
    """用表面蛋白 marker 规则定义参考细胞类型(marker 组合按数据集 panel 指定)。"""
    idx = {m.split("_")[0]: i for i, m in enumerate(markers)}

    def z(v):
        return (v - v.mean()) / v.std()

    def sc_(names):
        cols = [z(X_adt[:, idx[n]]) for n in names if n in idx]
        return sum(cols) if cols else np.zeros(X_adt.shape[0])

    score_map = {cell_type: sc_(ms) for cell_type, ms in marker_sets.items()}
    S = np.stack(list(score_map.values()), axis=1)
    names = list(score_map.keys())
    best, bestv = S.argmax(axis=1), S.max(axis=1)
    return np.where(bestv > 1.0, np.array(names)[best], "other")


def main(name="pbmc5k"):
    cfg = DATASETS[name]
    download_if_needed(cfg)

    # ---- 读取 10x 文件(RNA 与 ADT 在同一个矩阵中,按 feature_types 区分)----
    adata = sc.read_10x_h5(cfg["h5"], gex_only=False)
    adata.var_names_make_unique()
    gex = adata[:, adata.var["feature_types"] == "Gene Expression"].copy()
    adt = adata[:, adata.var["feature_types"] == "Antibody Capture"].copy()

    # ---- 基础 QC:去掉基因数过少的细胞、在过少细胞中出现的基因 ----
    sc.pp.filter_cells(gex, min_genes=200)
    sc.pp.filter_genes(gex, min_cells=3)
    adt = adt[gex.obs_names]  # 两个 view 保留同一批细胞

    # ---- 记录 QC 指标(供教程演示"数据的性质")----
    lib_size = np.asarray(gex.X.sum(axis=1)).ravel().astype(np.float32)   # 每细胞总 UMI 数
    n_genes = np.asarray((gex.X > 0).sum(axis=1)).ravel().astype(np.float32)  # 每细胞检出基因数

    # ---- RNA view:文库大小标准化 -> log1p -> 选 1000 个高变基因 ----
    sc.pp.normalize_total(gex, target_sum=1e4)
    sc.pp.log1p(gex)
    sc.pp.highly_variable_genes(gex, n_top_genes=1000)
    X_rna = gex[:, gex.var["highly_variable"]].X.toarray().astype(np.float32)

    # ---- ADT view:CLR 变换(蛋白计数的标准做法;注意不能套用 RNA 的 log-normalize)----
    # CLR:每个细胞内,log1p(count) 减去该细胞所有蛋白的均值,消除组成偏差
    markers = [v for v in adt.var_names if not v.startswith("IgG")]  # 去掉同型对照
    A = adt[:, markers].X.toarray().astype(np.float32)
    logA = np.log1p(A)
    X_adt = (logA - logA.mean(axis=1, keepdims=True)).astype(np.float32)

    # ---- 参考标签:免疫学标准 marker 规则 ----
    labels = make_labels(X_adt, markers, cfg["markers"])

    u, c = np.unique(labels, return_counts=True)
    print("label counts:", dict(zip(u, c)))

    np.savez_compressed(cfg["out"], X_rna=X_rna, X_adt=X_adt,
                        labels=labels, adt_names=np.array(markers),
                        gene_names=gex.var_names[gex.var["highly_variable"]].to_numpy(),
                        lib_size=lib_size, n_genes=n_genes)
    print(f"saved {cfg['out']}: X_rna{X_rna.shape}, X_adt{X_adt.shape}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pbmc5k")
