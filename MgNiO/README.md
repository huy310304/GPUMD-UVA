# Results and Discussion 

In this study, various simulations were conducted with over 10 force parameters, yielding a substantial number of output files. Utilizing Python, the data was graphed and the thermal conductivity was analyzed to identify the consistent range for `k(w)` across different force values. Each force value underwent 10 simulations, and the results were averaged to determine the corresponding `k(w)` value.

The primary objective was to ascertain the appropriate force parameters that result in a consistent range of `k(w)` values while ensuring stability in the simulations.

Below are plots illustrating the spectral thermal conductivity `k(w)` over frequency `v(THz)`, with integrated values representing the actual thermal conductivity.

## Analysis of Small Force Values
| ![Label 1](https://github.com/huy310304/GPUMD-UVA/assets/114793725/49d000fc-5774-4be0-9951-14415618c36d) | ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/3e7edfb0-705c-4e93-9ac3-7d393cd84231) | 
|:----------------------:|:----------------------:|
| Average of 10 runs with `F = 0.000005`             | Average of 10 runs with `F = 0.000035`            |

The plots reveal that with lower force values (`F = 0.000005` and `F = 0.000035`), the results exhibit higher fluctuations. Conducting multiple runs (averaging 10 runs) was crucial to discern that these fluctuations tend to average around similar values, approximately 4.4 (the average of areas under all the graphs).

## Analysis of Larger Force Values
| ![Label 1](https://github.com/huy310304/GPUMD-UVA/assets/114793725/5a8d586b-1ab7-494a-a1f2-8ffda7986033) | ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/7cc19fd6-1a4e-46dc-bb80-6acb74e06ad4) | ![Label 3](https://github.com/huy310304/GPUMD-UVA/assets/114793725/49d4fdb9-25e8-4b90-9042-8330ae085760) |
|:----------------------:|:----------------------:| :----------------------:|
| Average of 10 runs with `F = 0.00007`             | Average of 10 runs with `F = 0.0001`            | Average of 10 runs with `F = 0.00014`            | 

We can clearly see that The larger F-values (0.0007 above) show more consistency with smaller standard deviation and errors bars, and the areas under all graphs also average to around 4.4

## Analysis of Even Larger Force Values
| ![Label 1](https://github.com/huy310304/GPUMD-UVA/assets/114793725/92d9e5bd-0b32-441e-9833-008297d763de) | ![Label 2](https://github.com/huy310304/GPUMD-UVA/assets/114793725/485fb436-11fe-4167-8398-d15eb2127fac) | ![Label 3](https://github.com/huy310304/GPUMD-UVA/assets/114793725/8840120f-4ce8-48fe-9b2f-bee6528b2cac) |
|:----------------------:|:----------------------:| :----------------------:|
| Average of 10 runs with `F = 0.0002`             | Average of 10 runs with `F = 0.0004`            | Average of 10 runs with `F = 0.0008`            | 

With Larger F=0.0004 or F=0.0008, the K(w) values seem to be inconsistent (especially with F=0.0008)

## Analysis of Spectral Heat Current (SHC) `k(ω)` with Varying External Forces

The graph below illustrates how the spectral heat current (SHC), `k(ω)`, varies in response to different external force (F) values applied to our MgNiO alloy simulations. This visualization is crucial for identifying optimal F-values that balance the system's stability and response accuracy.

![Spectral Heat Current vs. F-values](https://github.com/huy310304/GPUMD-UVA/assets/114793725/a7a929e8-7cc6-4ad3-9de3-e836c0865ee2)

The targeted range for F-values is between 0.000035 and 0.0003, with an ideal operational point near 0.00014. This specific value offers a balance, reducing fluctuations and improving consistency in the simulation outcomes, thereby enhancing the reliability of our thermal conductivity predictions.

## Future Work: Use the desired F-values of 0.00014 to perform simulations at different temperatures




