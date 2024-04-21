# Results and Discussion 

## Phase 1: Find Optimized Force Value F(Å-1) at T(K) = 300K for thermal properties of MgNiO

In this research, various simulations were conducted with over 10 force parameters with an `T(K) = 300K`, yielding a substantial number of output files. Utilizing Python, the data was graphed and the thermal conductivity was analyzed to identify the consistent range for `k(w)` across different force values. Each force value underwent 10 simulations, and the results were averaged to determine the corresponding `k(w)` value.

The primary objective was to ascertain the appropriate force parameters `F(Å-1)` that result in a consistent range of `k(w)` values while ensuring stability in the simulations.

Below are plots illustrating the spectral thermal conductivity `k(w)` over frequency `v(THz)`, with integrated values representing the actual thermal conductivity.

### Analysis of Small Force Values
| ![Label 1](https://github.com/huy310304/GPUMD-UVA/assets/114793725/49d000fc-5774-4be0-9951-14415618c36d) | ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/3e7edfb0-705c-4e93-9ac3-7d393cd84231) | 
|:----------------------:|:----------------------:|
| Average of 10 runs with `F(Å-1) = 0.000005`             | Average of 10 runs with `F(Å-1) = 0.000035`            |

The plots reveal that with lower force values (`F(Å-1) = 0.000005` and `F(Å-1) = 0.000035`), the results exhibit higher fluctuations. Conducting multiple runs (averaging 10 runs) was crucial to discern that these fluctuations tend to average around similar values, approximately 4.4 (the average of areas under all the graphs).

### Analysis of Larger Force Values
| ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/7cc19fd6-1a4e-46dc-bb80-6acb74e06ad4) | ![Label 3](https://github.com/huy310304/GPUMD-UVA/assets/114793725/49d4fdb9-25e8-4b90-9042-8330ae085760) |
|:----------------------:| :----------------------:|
 | Average of 10 runs with `F(Å-1) = 0.0001`            | Average of 10 runs with `F(Å-1) = 0.00014`            | 

We can clearly see that The larger F-values (0.0007 above) show more consistency with smaller standard deviation and errors bars, and the areas under all graphs also average to around 4.4

### Analysis of Even Larger Force Values
| ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/485fb436-11fe-4167-8398-d15eb2127fac) | ![Label 3](https://github.com/huy310304/GPUMD-UVA/assets/114793725/8840120f-4ce8-48fe-9b2f-bee6528b2cac) |
|:----------------------:|:----------------------:|
| Average of 10 runs with `F(Å-1) = 0.0004`            | Average of 10 runs with `F(Å-1) = 0.0008`            | 

With Larger F(Å-1) = 0.0004 or F(Å-1) = 0.0008, the K(w) values seem to be inconsistent (especially with F=0.0008)

### Analysis of Spectral Heat Current (SHC) `k(ω)` with Varying External Forces

The graph below illustrates how the spectral heat current (SHC), `k(ω)`, varies in response to different external force (F) values applied to our MgNiO alloy simulations. This visualization is crucial for identifying optimal F-values that balance the system's stability and response accuracy.

![Spectral Heat Current vs. F-values](https://github.com/huy310304/GPUMD-UVA/assets/114793725/a7a929e8-7cc6-4ad3-9de3-e836c0865ee2)


## Conclusions
The targeted range for F-values is between 0.000035 and 0.0003, with an ideal operational point near 0.00014. This specific value offers a balance, reducing fluctuations and improving consistency in the simulation outcomes, thereby enhancing the reliability of our thermal conductivity predictions. 
| ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/386f0bf0-10cc-412e-aa3a-5f7212b7d678) |
|:----------------------:|
| Average of 10 runs with `F(Å-1) = 0.00014`            | 

<br>

## Phase 2: Exploring Thermal Properties of MgNiO at Varied Temperatures (100K - 900K)

After establishing that F(Å-1) = 0.00014 is the optimized force parameter at T(K) = 300K, we expanded the study to include a broader range of temperatures to understand how temperature impacts the thermal conductivity of MgNiO.

### Hypothesized Impact of Temperature on Thermal Conductivity
As temperature increases, so does the amplitude of lattice vibrations within materials. This results in more frequent and intricate phonon scattering, which can significantly disrupt thermal energy transfer, typically reducing the material's thermal conductivity.

### Methodology for Multi-Temperature Analysis
Using F(Å-1) = 0.00014 as a baseline force value, simulations were run at five temperatures: 100K, 300K, 500K, 700K, and 900K. This uniform approach initially helped identify the need for temperature-specific optimizations.

#### Initial Findings Using a Uniform Force Value
![Temperature vs. Thermal Conductivity Plot](https://github.com/huy310304/GPUMD-UVA/assets/114793725/85900522-3d12-41fc-8fe7-82f5b774ed61)

The graph above shows the results of these simulations. Despite using a consistent force value, the significant variation in `k(w)` suggests that each temperature may actually require a uniquely optimized force value to achieve reliable and consistent data.

### Optimizing Force Values for Each Temperature
Recognizing the inconsistency in the initial data, we undertook a detailed investigation to find the optimal force values for the temperatures at the extremes of our study range, namely 100K and 900K. This approach provided foundational data points from which we could interpolate optimal values for the intermediate temperatures using a line of best fit.

#### Specific Results for 100K and 900K
From the extensive simulations at the temperature extremes, optimized force values were determined. At T(K) = 100K, the optimized force value was found to be F(Å-1) = 0.0001, and for T(K) = 900K, it was F(Å-1) = 0.0004. These results provide key data points for understanding how force requirements change with temperature.

| ![Optimized F for 100K](https://github.com/huy310304/GPUMD-UVA/assets/114793725/39bc48a0-fa86-4a74-96c3-98afc4bc21a5) | ![Optimized F for 900K](https://github.com/huy310304/GPUMD-UVA/assets/114793725/83651af1-9d92-4541-98cc-067089c08cba) |
|:----------------------:|:----------------------:|
| `k(ω)` vs. F-values for `T(K) = 100K` | `k(ω)` vs. F-values for `T(K) = 900K` |

### Establishing a Best Fit Line for Optimized Forces Across Temperatures
Observing that the optimized F-values tend to increase linearly with temperature, a line of best fit was plotted to predict intermediate values, providing a strategic guide for setting force parameters at other temperatures.

![Line of Best Fit for Optimized Forces](https://github.com/huy310304/GPUMD-UVA/assets/114793725/4d1a573e-8e7f-43e6-a8b3-25dc71be6bbd)

### Applying the Predicted Force Values
With the best-fit line in place, optimized forces for 500K and 700K were predicted to be 0.00024Å and 0.00032Å and used in further simulations.

#### Validation Results for 500K and 700K
| ![500K Validation](https://github.com/huy310304/GPUMD-UVA/assets/114793725/ea146a78-8286-4aee-a2a0-1ea500a5cdae) | ![700K Validation](https://github.com/huy310304/GPUMD-UVA/assets/114793725/9709d81c-5856-45d9-9230-37211b811585) |
|:----------------------:|:----------------------:|
| Results for `T(K) = 500K` with `F(Å-1) = 0.00024` | Results for `T(K) = 700K` with `F(Å-1) = 0.00032` |

These results confirmed the hypothesis that tailored force values enhance the consistency and reliability of the simulations, as well as the linearly relationship between the optimized force value and temperature.

### Comprehensive Analysis of Temperature vs. Thermal Conductivity
The optimized force values were utilized to re-evaluate the thermal conductivity at each temperature, providing insight into how MgNiO's thermal properties respond to temperature and force parameter adjustments. The graph below demonstrates a more consistent trend in `k(w)` with smaller error bars, maintaining the expected decreasing behavior as `T(K)` increases.

![Comprehensive Thermal Conductivity Analysis](https://github.com/huy310304/GPUMD-UVA/assets/114793725/85be649f-e2e9-4e4b-8dc8-49c78dad723b)

This detailed visualization emphasizes the critical role of optimizing force parameters in computational material science. It enables the prediction and understanding of material behaviors under various thermal conditions.

TODO: Đợi 700K .32 chạy Run4 với đợi 900K .4 chạy Run4 với Run5, plotavg, plot3D



