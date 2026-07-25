---
layout: project
title: "SpudCell Whole Cell Cycle ODE Analysis"
year: 2024
topic: "cell-cycle-modeling"
authors: ["Pebble Team", "Summer School Students"]
status: "completed"
tags: [cell-biology, ode-modeling, jupyter-notebook, python]
project_image: "spudcell-preview.png"
date: 2024-07-25
---

# SpudCell Whole Cell Cycle ODE Analysis

## Project Overview

This project focuses on modeling the complete cell cycle using Ordinary Differential Equations (ODEs) to understand cell division dynamics and regulatory mechanisms.

## Research Context

**Scientific Question**: How can we model the complete cell cycle to understand the regulatory networks controlling cell division?

**Methods**: We developed a comprehensive ODE-based model that captures the key transitions and regulatory points in the cell cycle, including G1, S, G2, and M phases.

**Key Results**: The model successfully reproduces known cell cycle behaviors and provides predictions for intervention points.

## Project Materials

### 📊 Presentations
- [Main Tutorial Presentation](summerschool/2024/spudcell-tutorials/presentations/260725_spudecell_tutorials.pptx) - Comprehensive tutorial on SpudCell modeling
- [Methodology Overview](summerschool/2024/spudcell-tutorials/presentations/methodology-slides.pptx) - Detailed methodology and theoretical background

### 💻 Code & Analysis
- [Main Analysis Notebook](summerschool/2024/spudcell-tutorials/notebooks/spudcell_whole_cell_cycle_ODE.ipynb) - Interactive Jupyter notebook with ODE analysis
- [Simulation Scripts](summerschool/2024/spudcell-tutorials/notebooks/spudcell_simulation_results.csv) - Simulation results and outputs
- [Trajectory Data](summerschool/2024/spudcell-tutorials/notebooks/spudcell_ODE_trajectories.csv) - Cell cycle trajectory data

### 📈 Data & Outputs
- [ODE Generation Endpoints](summerschool/2024/spudcell-tutorials/manuscripts/spudcell_ODE_generation_endpoints.csv) - Key endpoints from ODE generation
- [Simulation Results](summerschool/2024/spudcell-tutorials/notebooks/spudcell_simulation_results.csv) - Complete simulation dataset

## Technical Implementation

### Model Components
- **ODE System**: 15 coupled differential equations
- **Parameters**: 32 kinetic parameters
- **Variables**: Cell cycle regulators, cyclins, checkpoints

### Software Requirements
```bash
pip install numpy pandas matplotlib scipy jupyter
```

### Running the Analysis
1. Clone this repository and navigate to the project directory
2. Install required dependencies: `pip install -r requirements.txt`
3. Open the Jupyter notebook: `jupyter notebook summerschool/2024/spudcell-tutorials/notebooks/spudcell_whole_cell_cycle_ODE.ipynb`

## Key Findings

1. **Cell Cycle Transitions**: Modeled transitions between G1, S, G2, and M phases
2. **Checkpoint Behavior**: Implemented G1/S and G2/M checkpoint controls
3. **Parameter Sensitivity**: Identified critical parameters affecting cycle duration
4. **Bifurcation Analysis**: Found parameter regions leading to different cycle behaviors

## Applications

This model can be used for:
- Understanding cell cycle regulation in normal and cancer cells
- Predicting effects of cell cycle inhibitors
- Designing experiments to test cell cycle hypotheses
- Teaching computational biology and ODE modeling

## Project Team

- **Instructors**: [Instructor Names]
- **Students**: Summer School 2024 Participants
- **Institution**: [Your Institution]

## Future Directions

- Extend model to include DNA damage response
- Incorporate spatial aspects of cell cycle
- Validate with experimental data
- Develop GUI for parameter exploration

---
*Part of Summer School 2024 - Cell Cycle Modeling Workshop*
*Last updated: July 25, 2024*
