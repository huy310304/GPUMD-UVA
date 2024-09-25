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

# Volume data from the simulations
volumes_300K = [
    42.80837728520066 * 42.80069979219133 * 42.819146497408,  # Ni_0.1_Zn_0.3 (400Ni - 1200Zn)
    42.73557981 * 42.73557981 * 42.73557981, # NPT expanded volume (J14)
    42.67976316972 * 42.6597354759144 * 42.6562987549984,    # Ni_0.3_Zn_0.1 (1200Ni - 400Zn)
]

# Calculating percentage differences relative to J14 model
j14_volume = volumes_300K[1]
volume_percentage_differences = [(vol - j14_volume) / j14_volume * 100 for vol in volumes_300K]

# Data for Lx, Ly, Lz for each composition
Lx_values = [42.80837728520066, 42.73557981, 42.67976316972]
Ly_values = [42.80069979219133, 42.73557981, 42.6597354759144]
Lz_values = [42.819146497408, 42.73557981, 42.6562987549984,]

# Create a plot for the volumes with adjusted label positions and distinct colors for each point
plt.figure(figsize=(10, 6))
x_ordered = np.arange(len(models_ordered))

# Plot the volumes
plt.plot(x_ordered, volumes_300K, '-o', color='red', markersize=15, linewidth=2, label="Volume at 300K")

# Add labels with distinct colors and positions for each composition
# 400Ni and 1200Zn: label below and to the right in purple
plt.text(x_ordered[0], volumes_300K[0], f"Lx={Lx_values[0]:.2f} Å\nLy={Ly_values[0]:.2f} Å\nLz={Lz_values[0]:.2f} Å\n+{volume_percentage_differences[0]:.2f}%", 
         ha='left', va='top', fontsize=10, color='purple', bbox=dict(facecolor='white', alpha=0.5, edgecolor='purple'))

# J14: label below and centered in green
plt.text(x_ordered[1], volumes_300K[1], f"Lx={Lx_values[1]:.2f} Å\nLy={Ly_values[1]:.2f} Å\nLz={Lz_values[1]:.2f} Å\n{volume_percentage_differences[1]:.2f}%", 
         ha='center', va='top', fontsize=10, color='green', bbox=dict(facecolor='white', alpha=0.5, edgecolor='green'))

# 1200Ni and 400Zn: label above and middle in orange
plt.text(x_ordered[2], volumes_300K[2], f"Lx={Lx_values[2]:.2f} Å\nLy={Ly_values[2]:.2f} Å\nLz={Lz_values[2]:.2f} Å\n{volume_percentage_differences[2]:.2f}%", 
         ha='center', va='bottom', fontsize=10, color='blue', bbox=dict(facecolor='white', alpha=0.5, edgecolor='orange'))

# Adding labels, title, and a legend
plt.xticks(x_ordered, models_ordered, rotation=0, ha='center', fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel('Volume (Å³)', fontsize=14)
plt.title('Volume at 300K with Lx, Ly, Lz and % Differences', fontsize=16)
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Adding a legend explaining the label colors
plt.legend(['Volume at 300K', 'Lx, Ly, Lz, % Differences'], loc="upper right", fontsize='large', frameon=True, shadow=True)

plt.tight_layout()
plt.show()

