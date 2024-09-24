import matplotlib.pyplot as plt
import numpy as np

# Data for the models
models_ordered = [
    """(Mg₀.₂Co₀.₂Ni₀.₁Cu₀.₂Zn₀.₃)O 
    (400 Ni and 1200 Zn)""",
    """(Mg₀.₂Co₀.₂Ni₀.₂Cu₀.₂Zn₀.₂)O (J14)
    (800 Ni and 800 Zn)""",
    """(Mg₀.₂Co₀.₂Ni₀.₃Cu₀.₂Zn₀.₁)O
    (1200 Ni and 400 Zn)"""
]

# Thermal conductivities and errors
thermal_conductivities_ordered = [2.580, 2.634, 2.655]
errors_ordered = [0.045, 0.055, 0.045]

# Calculating percentage differences relative to J14 model
j14_tc = thermal_conductivities_ordered[1]  # J14 model
percentage_differences_ordered = [(tc - j14_tc) / j14_tc * 100 for tc in thermal_conductivities_ordered]

# Creating the line plot for ordered thermal conductivities with custom colors and a legend
plt.figure(figsize=(10, 6))
x_ordered = np.arange(len(models_ordered))

# Plotting with error bars and markers, using distinct colors
plt.errorbar(x_ordered, thermal_conductivities_ordered, yerr=errors_ordered, fmt='-o', color='purple', ecolor='orange', capsize=5, markersize=10, linewidth = 2, label="Thermal Conductivity")

# Adding labels, title, and a legend
plt.xticks(x_ordered, models_ordered, rotation=0, ha='center', fontsize = 12)
plt.yticks(fontsize=12)
plt.ylabel('Thermal Conductivity (W/mK)', fontsize = 14)
plt.title('Thermal Conductivity of Various Models J14 Tuning Models', fontsize = 16)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(loc="upper left", fontsize='large', frameon=True, shadow=True)

plt.axhline(2.634, color='black', linestyle='--', linewidth=1.2)

plt.tight_layout()

# Display the thermal conductivity plot
plt.show()

# Line plot for ordered percentage differences with additional clarity and enhancements
plt.figure(figsize=(10, 6))

# Plotting percentage differences with larger markers and improved grid
plt.plot(x_ordered, percentage_differences_ordered, '-o', color='darkblue', markersize=10, linewidth=2, label="Percentage Difference")

# Adding labels, title, and enhanced legend
plt.xticks(x_ordered, models_ordered, rotation=0, ha='center', fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel('Percentage Difference (%)', fontsize=14)
plt.title('Percentage Difference in Thermal Conductivity Relative to J14 Model', fontsize=16)
plt.grid(True, which='both', linestyle='--', linewidth=0.7)
plt.legend(loc="upper left", fontsize='large', frameon=True, shadow=True)

# Add horizontal line for zero percentage difference to highlight comparison with J14
plt.axhline(0, color='black', linestyle='--', linewidth=1.2)

plt.tight_layout()

# Display the percentage difference plot
plt.show()


