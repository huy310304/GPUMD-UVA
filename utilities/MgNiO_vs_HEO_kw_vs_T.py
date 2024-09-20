# Plot with adjustments for larger ticks and bold axes
import numpy as np
import matplotlib.pyplot as plt

# Data for HEO
HEO_x_values = np.array([300, 500, 700, 900])
HEO_kw = np.array([2.502, 2.641, 2.414, 2.384])
HEO_F_values = np.array([0.00018, 0.00024, 0.00032, 0.0004])
HEO_errors = np.array([0.062, 0.066, 0.032, 0.011])

# Data for MgNiO
MgNiO_x_values = np.array([100, 300, 500, 700, 900])
MgNiO_kw = np.array([4.968, 4.304, 3.925, 3.507, 3.474])
MgNiO_F_values = np.array([0.0001, 0.00014, 0.00024, 0.00032, 0.0004])
MgNiO_errors = np.array([0.111, 0.097, 0.063, 0.051, 0.040])

# Data for CoNiO
CoNiO_x_values = np.array([300, 500])
CoNiO_kw = np.array([14.512, 10.257])
CoNiO_F_values = np.array([0.00008, 0.00015])
CoNiO_errors = np.array([0.190, 0.157])

# Plot the HEO data
plt.errorbar(HEO_x_values, HEO_kw, yerr=HEO_errors, fmt='o', markersize=8, color='blue', 
             label='HEO', markerfacecolor='none', capsize=5)

# Plot the MgNiO data
plt.errorbar(MgNiO_x_values, MgNiO_kw, yerr=MgNiO_errors, fmt='s', markersize=8, color='green', 
             label='MgNiO', markerfacecolor='none', capsize=5)

# Plot the CoNiO data
plt.errorbar(CoNiO_x_values, CoNiO_kw, yerr=CoNiO_errors, fmt='x', markersize=8, color='red', 
             label='CoNiO', markerfacecolor='none', capsize=5)

# Add labels and title with bold axes
plt.xlabel('Temperature (K)', fontsize=24)
plt.ylabel('Thermal Conductivity k(w) (W/mK)', fontsize=24)
plt.title('Thermal Conductivity vs. Temperature using Optimized F', fontsize=24)

# Set the font size and bold for x-axis and y-axis numbers
plt.xticks(fontsize=24, fontweight='bold')
plt.yticks(fontsize=24, fontweight='bold')

# Annotate each point with its coordinates for HEO
for x, y, z in zip(HEO_x_values, HEO_kw, HEO_F_values):
    plt.annotate(f'({x}, {y:.3f}, {z})', (x, y), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=12, color='blue')

# Annotate each point with its coordinates for MgNiO
for x, y, z in zip(MgNiO_x_values, MgNiO_kw, MgNiO_F_values):
    plt.annotate(f'({x}, {y:.3f}, {z})', (x, y), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=12, color='green')

# Annotate each point with its coordinates for CoNiO
for x, y, z in zip(CoNiO_x_values, CoNiO_kw, CoNiO_F_values):
    plt.annotate(f'({x}, {y:.3f}, {z})', (x, y), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=12, color='red')

# Set the limits of y-axis and set to log scale
plt.yscale('log')
plt.ylim(0.1, 100)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add legend for the plotted data
plt.legend(fontsize=16)

# Add an additional text box legend explaining the three numbers
textstr = (
    "Legend for Annotations:\n"
    "1st: Temperature (K)\n"
    "2nd: Thermal Conductivity (W/mK)\n"
    "3rd: Optimized Force (Å⁻¹)"
)
plt.gcf().text(0.7, 0.65, textstr, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

# Display the plot
plt.show()
