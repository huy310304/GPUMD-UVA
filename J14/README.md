# Results and Discussion for Thermal Conductivity of (Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O (J14) (In Progress)

## Phase 1: Exploring Thermal Properties of the J14 at Varied Temperatures (100K - 900K)

Building on the [Thermal Conductivity work of MgNiO](../MgNiO), we applied the optimized force parameters from MgNiO to a new alloy, referred to as J14. We obtained results for each temperature, using the optimized F-values from MgNiO as an educated starting point. However, due to the structural differences of the J14 alloy, adjustments may be necessary. Details of the approach for optimizing the forces across different temperatures can be found in the `Establishing a Best Fit Line for Optimized Forces Across Temperatures` section in the [MgNiO README file](https://github.com/huy310304/GPUMD-UVA/tree/main/MgNiO#establishing-a-best-fit-line-for-optimized-forces-across-temperatures).

### Results for 300K Using F-values of 0.00018

| ![Spectral Thermal Conductivity at 300K](https://github.com/user-attachments/assets/27c16b02-8d8c-4ad3-beab-1d7da170d5dd) | ![Thermal Conductivity at 300K](https://github.com/user-attachments/assets/dca578d5-e0b0-4dd2-861d-cadffe1047b3) |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| **Spectral Thermal Conductivity of 5 runs at `300K with F(Å⁻¹) = 0.00018`** | **Thermal Conductivity at `300K with F(Å⁻¹) = 0.00018`** |

From these results, we observe that the thermal conductivities are reasonable within a small error margin, and all runs were consistent. This suggests that the optimized force parameter for MgNiO may be close to the optimized force for the J14.

### Additional Results at Different Temperatures (500K, 700K, and 900K)

| ![Spectral Thermal Conductivity at 500K](https://github.com/user-attachments/assets/e3b2682d-dec3-487a-988e-017cbdeab7d5) | ![Thermal Conductivity at 500K](https://github.com/user-attachments/assets/d479b761-76a9-475f-8a7c-3c0bda09478a) |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| **Spectral Thermal Conductivity of 5 runs at `500K with F(Å⁻¹) = 0.00024`** | **Thermal Conductivity at `500K with F(Å⁻¹) = 0.00024`** |

| ![Spectral Thermal Conductivity at 700K](https://github.com/user-attachments/assets/22676c64-3b5e-48cc-9d83-1e89aefb19b7) | ![Thermal Conductivity at 700K](https://github.com/user-attachments/assets/9ff1e32a-ce73-477c-84ee-bf8b32428860) |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| **Spectral Thermal Conductivity of 5 runs at `700K with F(Å⁻¹) = 0.00032`** | **Thermal Conductivity at `700K with F(Å⁻¹) = 0.00032`** |

| ![Spectral Thermal Conductivity at 900K](https://github.com/user-attachments/assets/3d3d13f1-d63a-48b1-8863-57605713587d) | ![Thermal Conductivity at 900K](https://github.com/user-attachments/assets/2edf83a2-a752-4464-b7a4-2bee7d292c6c) |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| **Spectral Thermal Conductivity of 5 runs at `900K with F(Å⁻¹) = 0.0004`** | **Thermal Conductivity at `900K with F(Å⁻¹) = 0.0004`** |

All these results exhibit a high level of consistency across multiple runs, with minimal variation between individual runs as indicated by the low error bars. This consistency suggests that the optimized force parameters effectively stabilize the thermal conductivity measurements for the J14 across the tested temperature range (300K - 900K).

### Comprehensive Analysis of Temperature vs. Thermal Conductivity

The results of the thermal conductivity across different temperatures were plotted together, and a clear trend emerges. Unlike the behavior observed in MgNiO, where increasing temperature typically results in lower thermal conductivity, the J14 shows relatively stable thermal conductivity across different temperatures. This suggests that the J14’s thermal properties are less sensitive to temperature changes compared to MgNiO.

| ![3D Plot](https://github.com/user-attachments/assets/a17cdcd5-d5ce-468f-bca7-48dd0bb2bf41) | ![Thermal Conductivity Table](https://github.com/user-attachments/assets/c1e1330b-7421-413a-82e0-286eaa6f96be) |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|

**3D Plot of Average Spectral Thermal Conductivity Across Temperatures Using Optimized Force Parameters**

#### Analysis of Trends

- **Stable Thermal Conductivity**: The thermal conductivity across temperatures shows less variation compared to MgNiO. This could be attributed to the high-entropy nature of the alloy, where the atomic disorder contributes to a more stable phonon scattering mechanism across temperatures. (See `Comprehensive Analysis of Temperature vs. Thermal Conductivity` section in the [MgNiO README file](https://github.com/huy310304/GPUMD-UVA/tree/main/MgNiO#comprehensive-analysis-of-temperature-vs-thermal-conductivity)).
  
- **Comparison with MgNiO**: The results suggest that while MgNiO shows a clear decrease in thermal conductivity with temperature, the J14 alloy maintains a more consistent thermal conductivity, potentially making it more suitable for applications requiring stable thermal performance across a wide temperature range.

- **Lower Thermal Conductivity**: The thermal conductivity of the J14 is generally lower than that of MgNiO, as shown in the graph below:

![Temperature vs Thermal Conductivity](https://github.com/user-attachments/assets/1dac5da3-0995-4a72-8a26-b572459b3ec0)

**Temperature vs. Thermal Conductivity for the J14 at Varied Temperatures**

### Conclusion for Phase 1

- The force parameters optimized for MgNiO were also applicable to the J14 , resulting in consistent thermal conductivity measurements across all temperatures and runs.
- The J14 demonstrates more consistent thermal conductivity across different temperatures compared to the decreasing trend observed in MgNiO.
- The thermal conductivity of the J14 is lower than that of MgNiO across the tested temperature range.
- These findings suggest that the J14 might be more suitable for applications where stable thermal performance is required across a wide temperature range.

## Phase 2: Tuning the Thermal Conductivity of the J14

In the next phase, we will explore how to tune the thermal conductivity of the J14 by adjusting the concentrations of its components. Specifically, we will investigate whether lowering the concentrations of Cu and Mg to 15% can increase the thermal conductivity, and whether increasing their concentrations to 25% can decrease the thermal conductivity. These experiments will be conducted at 500K as an illustrative example.
