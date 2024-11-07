# GPUMD-UVA (In-progress)

## 📝 [JAP Paper](https://doi.org/10.1063/5.0224282)

### Research Focus
The project, led by Professor Keivan Esfarjani, with Bikash Timalsina as the graduate student, focuses on investigating the thermal properties of high-entropy alloys (HEAs) using molecular dynamics (MD) simulations on UVA Afton High-Performance Computing system.

### Recent Work and Updates (Fall 2024)
- **NEP Training**: Conducting model generation by training a NEP potential model with extensive hyperparameter tuning to minimize energy and force loss results. The goal is to train a baseline model for HEO, then apply the same training process for CO2 and H2O data to get their model for molecular dynamics simulations.
- **Molecular Dynamics Simulations**: Focused on running MD simulations for **Co₀.₂₅Ni₀.₇₅O** and **(Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O** alloys using the **J14 potential** to investigate their thermal properties.
- **Composition Tuning**: Adjusted the atomic concentrations of Ni and Zn elements within the J14 potential to explore how thermal conductivity can be controlled. This involved studying the effects of varying concentrations on lattice distortion and analyzing the correlation between structural disorder and thermal conductivity.

### Tools and Methods
- **GPUMD** for efficient GPU-based MD simulations.
- **Python** and **MATLAB** for data analysis and visualization, automating thermal conductivity and energy loss graphs.
- **Linux commands** and **SLURM** for managing simulation jobs on the UVA **Afton** supercomputer.

### Simulation Tasks
- Conducted over **100 thermal simulations** for 4 HEAs (Mg₀.₅Ni₀.₅O, Co₀.₂₅Ni₀.₇₅O, J14, and J14 tuning).
- Optimized simulations with various runtime combinations and driving forces.
- Repeated simulations across different temperature ranges (100K-900K).

### Visualization and Analysis
- Generated multiple graphs to visualize thermal conductivity and spectral heat currents at various temperatures.
- Automated analysis using Python and MATLAB, producing over 300 visual summaries of simulation results.

## Simulation Results and Discussions
- ### [Mg₀.₅Ni₀.₅O Potential](./MgNiO/)
- ### [Co₀.₂₅Ni₀.₇₅O Potential](./CoNiO/)
- ### [(Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O - J14 Potential and Tuning](./J14/)
- ### [Data Collection and Analysis Slides - Uncleaned Version](./slides)

## References
### Documents and Tutorials
- #### [GPUMD Document Page](https://gpumd.org/index.html)
- #### [NEMD Running Tutorial](https://gpumd.org/tutorials/thermal_transport_nemd.html)
- #### [HNEMD Running Tutorial](https://gpumd.org/tutorials/thermal_transport_hnemd.html)
- #### [GPUMD Source Code](https://github.com/brucefan1983/GPUMD)
- #### [UVA Afton](https://www.rc.virginia.edu/userinfo/rivanna/overview/)
### Related Papers
- #### [Charge-Induced Disorder Controls the Thermal Conductivity of Entropy-Stabilized Oxides](https://onlinelibrary.wiley.com/doi/10.1002/adma.201805004)
