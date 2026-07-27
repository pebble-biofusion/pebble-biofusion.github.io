# Bridge Omics to Mechanism

This package contains two self-contained teaching notebooks and their local
data files.

## Run

1. Extract the complete ZIP archive. Do not open a notebook while it is still
   inside the archive.
2. Keep the `data` folder beside `student.ipynb` and `solutions.ipynb`.
3. Open a terminal in the extracted `Bridge_omics_to_mechanism` folder.
4. Install the environment and start Jupyter:

```bash
python -m pip install -r requirements.txt
python -m jupyter lab
```

Open `student.ipynb` for the exercise or `solutions.ipynb` for the worked
analysis. After the packages are installed, the notebooks require no network
access.

## Package layout

```text
Bridge_omics_to_mechanism/
├── README.md
├── requirements.txt
├── student.ipynb
├── solutions.ipynb
└── data/
    ├── u2os_cell_cycle_blind.h5ad
    ├── u2os_fucci_reveal.csv.gz
    ├── human_cd34_bone_marrow_blind.h5ad
    └── human_cd34_reference_reveal.csv.gz
```

The `reveal` tables are held-out reference information. The notebooks locate
all four files relative to the extracted package and do not require paths from
the original repository.
