# Thermal Conductivity Plotting using Optimized Force Parameters

## Overview

This generates two types of plots for analyzing thermal conductivity data using optimized force parameters:

1. **2D Plot: K(w) vs Temperature (300K - 500K)**:
   - The plot displays K(w) values at specific temperatures with error bars.
   - Logarithmic scaling is applied to the y-axis, and the data points are annotated with their corresponding values.

2. **3D Plot: K(w) vs Frequency (ν) across Temperatures (300K & 500K)**:
   - The 3D plot shows how thermal conductivity k(w) varies with frequency nu across different temperatures.
   - Each temperature (300K and 500K) is plotted with thick lines, using sample data loaded from `.npy` files.

### Usage

To generate the plots:
1. Ensure you have the required `.npy` data files for each temperature (e.g., `shc_kw_avg_300K_Optimized_F.npy`, `shc_nu_avg_300K_Optimized_F.npy`).
2. Run the script to visualize the 2D and 3D plots.

### Libraries Used
- `numpy`: For data loading and manipulation.
- `matplotlib`: For plotting 2D and 3D graphs.

