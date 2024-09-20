# GPUMD-UVA (In-progress)

## 📝 [A brief summarization poster](https://drive.google.com/file/d/1gUmejQSglso3Zh1EY1O8N_IgMgXjIA_r/view?usp=sharing)

### Research Focus
The project, led by Professor Keivan Esfarjani, with Bikash Timalsina as the graduate student, focuses on investigating the thermal properties of high-entropy alloys (HEAs) using molecular dynamics (MD) simulations.

### Recent Work and Updates (Summer 2024)
- **Molecular Dynamics Simulations**: Focused on running MD simulations for **Co₀.₂₅Ni₀.₇₅O** and **(Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O** alloys using the **J14 potential** to investigate their thermal properties.
- **Composition Tuning**: Adjusted the atomic concentrations of Ni and Zn elements within the J14 potential to explore how thermal conductivity can be controlled. This involved studying the effects of varying concentrations on lattice distortion and analyzing the correlation between structural disorder and thermal conductivity.

### Tools and Methods
- Utilized the **GPUMD** package, Python, MATLAB, and Linux commands for simulation tasks.
- **GPUMD** provided efficient MD simulation capabilities.
- Python and MATLAB facilitated data analysis and visualization.
- Linux commands were used to manage and execute simulations on the UVA **Rivanna** supercomputer.

### Simulation Tasks
- Conducted over 30 thermal simulations for different HEAs.
- Optimized simulations with various combinations of driving forces and runtimes for each alloy.
- Repeated the process for different temperature ranges.

### Visualization and Analysis
- Generated numerous graphs for each simulation of different alloys at different temperatures to visualize thermal conductivity and spectral heat currents over the production time.

## Simulation Results and Discussions
- ### [Mg₀.₅Ni₀.₅O Potential](./MgNiO/)
- ### [Co₀.₂₅Ni₀.₇₅O Potential](./CoNiO/)
- ### [(Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O - J14 Potential](./J14/)

## References
### Documents and Tutorials
- #### [GPUMD Document Page](https://gpumd.org/index.html)
- #### [NEMD Running Tutorial](https://gpumd.org/tutorials/thermal_transport_nemd.html)
- #### [HNEMD Running Tutorial](https://gpumd.org/tutorials/thermal_transport_hnemd.html)
- #### [GPUMD Source Code](https://github.com/brucefan1983/GPUMD)
- #### [UVA Rivanna](https://www.rc.virginia.edu/userinfo/rivanna/overview/)
### Related Papers
- #### [Charge-Induced Disorder Controls the Thermal Conductivity of Entropy-Stabilized Oxides](https://onlinelibrary.wiley.com/doi/10.1002/adma.201805004)
