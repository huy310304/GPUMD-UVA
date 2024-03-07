# MgNiO Alloy Simulation 

This describes the process for conducting non-equilibrium simulations of MgNiO alloy under various external forces on UVA Rivanna.

## Preparation

- **Model Generation**: Create `model.xyz` and `nep.txt` for the initial structure and settings.

## Execution

- **Setup**: Prepare `run.in` and `run.slurm` for each simulation.
- **Launch**: Submit the job with `sbatch run.slurm`. Each run takes ~20 hours and can be modified.

## Repetition

- Perform 10 runs per F-value for statistical reliability.

## Analysis

- **Data Extraction**: After completion, extract data from output files (`shc.out` and `kappa.out`)
- **Graphing**: Use Python `plot_diffusive.py` to plot `k(ω)` vs. `ν(THz)`.

## Sample Simulations

Included is a directory for F-value = 0.00014 as a reference.
