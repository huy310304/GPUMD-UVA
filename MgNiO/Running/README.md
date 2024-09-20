# MgNiO Alloy Simulation Setup

## [See Results Here](../)

This document provides an overview of the process for conducting Thermal Transport simulations, including Non-Equilibrium Molecular Dynamics (NEMD) and Heat-Flux Nonequilibrium Molecular Dynamics (HNEMD), of the MgNiO alloy under various external forces. All simulations are performed on the UVA Rivanna HPC system.

## Model and Potential Preparation

- **Model Generation**: The initial structure and potential (`model.xyz` and `nep.txt`) are generated using machine learning techniques. These files are typically created by a graduate student and serve as the input for subsequent simulations.

## Running the MD Simulations

### Step 1: NEMD Simulation

The **Thermal Transport NEMD** process is run first by following the [NEMD tutorial](https://gpumd.org/tutorials/thermal_transport_nemd.html). This simulation provides the data required for analyzing thermal conductance.

- **Output**: After completing the NEMD simulation, run the `plot_ballistic.py` script, which stores the thermal conductance data in `Gc.npy` in the `ballistic` directory.

### Step 2: HNEMD Simulation

Next, perform the **Homogeneous NEMD (HNEMD)** simulation by following the [HNEMD tutorial](https://gpumd.org/tutorials/thermal_transport_hnemd.html). This step focuses on thermal transport under homogeneous conditions.

- [**Input Files**](https://gpumd.org/gpumd/input_files/)
- [**Output Files**](https://gpumd.org/gpumd/output_files/)

## Post-Simulation: Data Extraction and Analysis

After each run, we extract critical data for analysis:

1. **Thermal Conductivity Data Extraction**:
   - Retrieve `kappa.out`, `shc_nu.out`, and `shc_kw.out` from each run. These files contain spectral thermal conductivity data (`k(ω)`), frequencies (`ν`), and other thermal transport metrics.
   
2. **Averaging the Results**:
   - Perform 10 runs for each force value (`F`) to ensure statistical reliability. 
   - Average the data across all runs to get consistent and reliable results.

3. **Plotting**:
   - Use the `plot_diffusive.py` script to generate a plot of the spectral thermal conductivity (`k(ω)`) versus frequency (`ν (THz)`).
   - The averaged values of `shc_nu` and `shc_kw` from all runs are used to create these plots.

4. **Thermal Conductivity Calculation**:
   - Integrate the `kappa` values over the spectral thermal conductivity plot to compute the total thermal conductivity of the material.

## Repetition and Reliability

- For each force value (`F`), the simulation process is repeated 10 times to ensure the reliability and consistency of the results.
- Each run contributes to calculating an averaged thermal conductivity value.

## Sample Simulations

You can find a reference directory for `F = 0.00014` at `T = 300K` in the [Run_F=0.00014](./Run_F=0.00014) folder. This directory includes input files, output data, and plots for comparison and analysis.
