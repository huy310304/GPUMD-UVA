import numpy as np
import matplotlib.pyplot as plt

# Sample data for the line
x_values = np.array([300, 500])
kw = np.array([14.512, 10.257])
F_values = np.array([0.00008, 0.00015])

# Data for the error bars
errors = np.array([0.190, 0.157])

# Plot the points with "x" marks
plt.errorbar(x_values, kw, yerr=errors, fmt='x', markersize=10, color='red', label='Points')

# Plot the error bars with different color
plt.errorbar(x_values, kw, yerr=errors, fmt='none', ecolor='orange', label='Error Bars')

# Add labels and title
plt.legend(fontsize=12)
plt.xlabel('Temp (K)', fontsize=20)
plt.ylabel('k(w) using integration', fontsize=20)
plt.title('K(w) versus Temp using optimized F', fontsize=20)

# Set the font size of x-axis numbers
plt.xticks(fontsize=12)

# Set the font size of y-axis numbers
plt.yticks([0, 1, 10, 100], fontsize=12)

# Annotate each point with its coordinates
for x, y, z in zip(x_values, kw, F_values):
    plt.annotate(f'({x}, {y:.3f}, {z})', (x, y), textcoords="offset points", xytext=(70, 30), ha='right', fontsize=12)

# Add legend
plt.legend(fontsize=15)
plt.yscale("log")
plt.ylim(0.1, 100)
plt.xlim(290, 510)

plt.grid(True)

# Display the plot
plt.show()
