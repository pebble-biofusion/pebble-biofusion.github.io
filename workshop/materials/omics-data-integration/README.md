# Data Integration for Omics — 学生版教程包

两个 30–35 分钟的数据整合教程（单模态 + 多模态),CPU 即可，零基础友好。

## 文件夹内容

| 文件 | 说明 |
|---|---|
| `interactive_tutorial.html` | **主教程**:Part I 单模态整合 + Part II 多模态整合的全部内容,含交互滑块(双击用浏览器打开即可,无需安装任何东西) |
| `exercise_pbmc10k.ipynb` | **学生练习**:在新数据集上独立完成整合流程(8 处填空 + 思考题,附折叠参考答案) |
| `citeseq_pbmc.npz` | 教程数据:PBMC 5k CITE-seq(5,197 细胞 × 1,000 基因 × 29 蛋白) |
| `citeseq_pbmc10k.npz` | 练习数据:PBMC 10k CITE-seq,不同供体(7,856 细胞 × 1,000 基因 × 14 蛋白) |
| `requirements.txt` | 练习 notebook 的依赖 |
| `prepare_data.py` | 从 10x 原始数据复现两个 npz 的预处理脚本 |

## 使用顺序

1. 用浏览器打开 `interactive_tutorial.html`,按 Part I → Part II 学习(约 70 分钟);
2. 动手练习:`pip install -r requirements.txt`,然后用 Jupyter 打开 `exercise_pbmc10k.ipynb`(约 40 分钟);
3. 所有数据本地自带,全程无需联网。

## 数据来源(可复现)

- PBMC 5k:10x Genomics, "5k PBMCs from a healthy donor, with cell surface proteins (v3)"
  https://cf.10xgenomics.com/samples/cell-exp/3.0.2/5k_pbmc_protein_v3/5k_pbmc_protein_v3_filtered_feature_bc_matrix.h5
- PBMC 10k:10x Genomics, "PBMCs from a healthy donor, with cell surface proteins (v3)"
  https://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_10k_protein_v3/pbmc_10k_protein_v3_filtered_feature_bc_matrix.h5

复现方式(需要 `pip install scanpy`,仅复现时需要):

```bash
python prepare_data.py          # 生成 citeseq_pbmc.npz
python prepare_data.py pbmc10k  # 生成 citeseq_pbmc10k.npz
```

## 备用运行方式

若本地环境配置遇到问题,可使用 Google Colab(colab.research.google.com):
上传 `exercise_pbmc10k.ipynb` 与两个 `.npz` 文件,代码无需修改即可运行。
