import numpy as np
import matplotlib.pyplot as plt

# Sample data for the line
x_values = np.array([100, 300, 500, 700, 900])
kw = np.array([4.968, 4.304, 3.925, 3.507, 3.474])
F_values = np.array([0.0001, 0.00014, 0.00024, 0.00032, 0.0004])

# Data for the error bars
errors = np.array([0.111, 0.097, 0.063, 0.051, 0.040])

# Plot the points with "x" marks
plt.errorbar(x_values, kw, yerr=errors, fmt='x', markersize=10, color='red', label='Points')

# Plot the error bars with different color
plt.errorbar(x_values, kw, yerr=errors, fmt='none', ecolor='orange', label='Error Bars')

# # Fit a polynomial of degree 3 (cubic fit)
# fit_coeffs = np.polyfit(x_values, kw, 3)

# Create a polynomial function using the fit coefficients
# fit_line = np.poly1d(fit_coeffs)

# Calculate the y values of the fit line
# fit_values = fit_line(x_values)

# # Plot individual lines connecting data points
# plt.plot(x_values, kw, linestyle='-', color='orange', label='Individual Lines')

# Plot the cubic fit line
# plt.plot(x_values, fit_values, color='green', linestyle='-', label='Cubic Fit')

# Constants
a = 0.0927535
b = 0.165869

# Define x range
x_fit_lines = np.linspace(100, 900, 400)  # more points for a smoother curve
y_fit_lines = 1 / (a * x_fit_lines**b)

# Plotting the fit line
plt.plot(x_fit_lines, y_fit_lines, label=f'$y = 1/({a:.7f}x^{{{b:.6f}}})$', linestyle='-', color='blue')

# Add labels and title
plt.legend(fontsize=12)

# Add labels and title
plt.xlabel('Temp (K)', fontsize=20)
plt.ylabel('k(w) using integration', fontsize=20)
plt.title('K(w) versus Temp using optimized F', fontsize=20)

# Set the font size of x-axis numbers
plt.xticks(fontsize=12)

# Set the font size of y-axis numbers
plt.yticks(fontsize=12)

# Annotate each point with its coordinates
for x, y, z in zip(x_values, kw, F_values):
    plt.annotate(f'({x}, {y:.3f}, {z})', (x, y), textcoords="offset points", xytext=(50, 20), ha='right', fontsize=12)

# Add legend
plt.legend(fontsize=15)

plt.grid(True)

# Display the plot
plt.show()
