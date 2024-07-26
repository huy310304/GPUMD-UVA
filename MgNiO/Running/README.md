# MgNiO Alloy Simulation Setup

## [See Results Here](../)

This document outlines the process for conducting Thermal Transport from Non-Equilibrium Molecular Dynamics (NEMD) and Heat-Flux Nonequilibrium Molecular Dynamics (HNEMD) simulations of MgNiO alloy under various external forces on the UVA Rivanna HPC system.

## Model and Potential Preparation

- **Model Generation**: Generate `model.xyz` and `nep.txt` for the initial structure and settings through a machine learning process, typically conducted by a graduate student.

## Running the MD

The Thermal Transport NEMD Process is executed first by following the [NEMD tutorial](https://gpumd.org/tutorials/thermal_transport_nemd.html). This process produces the desired data for thermal conductance, stored in `Gc.npy` after running `plot_ballistic.py` (see the [NEMD directory](./ballistic))

Subsequently, the Homogeneous NEMD (HNEMD) Process is performed by following the [HNEMD tutorial](https://gpumd.org/tutorials/thermal_transport_hnemd.html).

- [**Input Files**](https://gpumd.org/gpumd/input_files/)
- [**Output Files**](https://gpumd.org/gpumd/output_files/)

## Repetition

- Perform 10 runs per force value (`F`) for statistical reliability.

## Analysis

- **Data Extraction**: Extract relevant data from output files (`shc.out` and `kappa.out`) after completion.
- **Graphing**: Utilize Python script `plot_diffusive.py` to plot the spectral thermal conductivity (`k(ω)`) against frequency (`ν(THz)`).
- **Averaging**: Average the results from across all the runs to determine and analyze the overall performance.

## Sample Simulations

(A directory)[./Run_F=0.00014] for `F = 0.00014` at `T = 300K` is included as a reference for comparison and analysis.

