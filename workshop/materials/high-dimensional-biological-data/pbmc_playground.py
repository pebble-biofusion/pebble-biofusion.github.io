"""Small, student-friendly helpers for the real-data PCA/t-SNE playground."""

from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.request import urlretrieve

import h5py
import numpy as np


PBMC3K_URL = (
    "https://zenodo.org/records/3752813/files/"
    "pbmc3k_processed.h5ad?download=1"
)
PBMC3K_MD5 = "091643725047edf7c1013e6e66d1b858"

CELL_TYPE_ORDER = [
    "B-cell",
    "CD4 T-cell",
    "CD8 T-cell",
    "CD14+ monocyte",
    "FCGR3A+ monocyte",
    "NK cell",
    "pDC",
]

PBMC_PALETTE = {
    "B-cell": "#4C78E8",
    "CD4 T-cell": "#18A6A6",
    "CD8 T-cell": "#55B86A",
    "CD14+ monocyte": "#F2B84B",
    "FCGR3A+ monocyte": "#F28E6B",
    "NK cell": "#8A63D2",
    "pDC": "#F05A9D",
}


def _md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_pbmc3k(cache_dir: str | Path) -> dict[str, np.ndarray | Path | bool]:
    """Download once, verify, and read the classroom PBMC3K data."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    data_path = cache_dir / "pbmc3k_processed.h5ad"
    downloaded = False

    if not data_path.exists():
        partial_path = data_path.with_suffix(".h5ad.part")
        urlretrieve(PBMC3K_URL, partial_path)
        partial_path.replace(data_path)
        downloaded = True

    checksum = _md5(data_path)
    if checksum != PBMC3K_MD5:
        raise RuntimeError(
            "PBMC3K checksum mismatch. Delete the cached file and run this cell again."
        )

    with h5py.File(data_path, "r") as handle:
        obs = handle["obs"][:]
        obsm = handle["obsm"][:]
        categories = np.array(
            [value.decode("utf-8") for value in handle["uns/celltype_categories"][:]]
        )
        labels = categories[obs["celltype"].astype(int)]
        expression = np.asarray(handle["X"], dtype=np.float32)
        pca = np.asarray(obsm["X_pca"], dtype=float)
        tsne = np.asarray(obsm["X_tsne"], dtype=float)

    return {
        "expression": expression,
        "pca": pca,
        "tsne": tsne,
        "cell_type": labels,
        "path": data_path,
        "downloaded": downloaded,
    }


def run_pca(
    expression: np.ndarray,
    n_components: int = 50,
    random_state: int = 7,
) -> np.ndarray:
    """Return a cells-by-components PCA representation."""
    from sklearn.decomposition import PCA

    model = PCA(
        n_components=n_components,
        svd_solver="randomized",
        random_state=random_state,
    )
    return model.fit_transform(np.asarray(expression, dtype=np.float32))


def run_tsne(
    features: np.ndarray,
    perplexity: float = 30,
    random_state: int = 7,
) -> np.ndarray:
    """Return a two-dimensional t-SNE representation."""
    from sklearn.manifold import TSNE

    model = TSNE(
        n_components=2,
        perplexity=perplexity,
        init="pca",
        learning_rate="auto",
        random_state=random_state,
    )
    return model.fit_transform(np.asarray(features, dtype=np.float32))
