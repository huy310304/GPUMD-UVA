# MgNiO Alloy Simulation Setup

# TODO: Add in Ovito and how to find parameters in plot_diffusive.py and plot_ballistic.py and load_shc.py

## [See Results Here](../)

This describes the process for conducting Thermal Transport from NEMD and HNEMD of MgNiO alloy under various external forces on UVA Rivanna. 

## Preparation

- **Model Generation**: Generate `model.xyz` and `nep.txt` for the initial structure and settings through machine learning process, conducted by a graduate student.

## Execution 

### NEMD Process
The NEMD Process is run first with the [NEMD tutorial](https://gpumd.org/tutorials/thermal_transport_nemd.html)  
The desired data for thermal conductance will then be produced in `Gc.npy` after running `plot_ballistic.py`

- [Input Files](https://gpumd.org/gpumd/input_files/)
- [Output Files](https://gpumd.org/gpumd/output_files/)

## Repetition

- Perform 10 runs per F-value for statistical reliability.

## Analysis

- **Data Extraction**: After completion, extract data from output files (`shc.out` and `kappa.out`)
- **Graphing**: Use Python `plot_diffusive.py` to plot `k(ω)` vs. `ν(THz)`.

## Sample Simulations

Included is a directory for F-value = 0.00014 at T = 300K as a reference.

