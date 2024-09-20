import numpy as np
import matplotlib.pyplot as plt

# Sample data for the line
x_values = np.array([100, 300, 500, 700, 900])
kw = np.array([5.669, 4.304, 4.168, 3.291, 3.293])

# Fit a polynomial of degree 3 (cubic fit)
# fit_coeffs = np.polyfit(x_values, kw, 3)

# Create a polynomial function using the fit coefficients
# fit_line = np.poly1d(fit_coeffs)

# Calculate the y values of the fit line
# fit_values = fit_line(x_values)

# Data for the error bars
errors = np.array([0.256, 0.096, 0.355, 0.106, 0.099])

# Plot the points with "x" marks
plt.errorbar(x_values, kw, yerr=errors, fmt='x', markersize=10, color='red', label='Points')

# Plot the error bars with different color
plt.errorbar(x_values, kw, yerr=errors, fmt='none', ecolor='orange', label='Error Bars')

# Plot individual lines connecting data points
# plt.plot(x_values, kw, linestyle='-', color='orange', label='Individual Lines')

# Plot the cubic fit line
# plt.plot(x_values, fit_values, color='green', linestyle='-', label='Cubic Fit')

# Add labels and title
plt.xlabel('Temp (K)', fontsize=20)
plt.ylabel('k(w) using integration', fontsize=20)
plt.title('K(w) versus Temp using F = 0.00014', fontsize=20)

# Set the font size of x-axis numbers
plt.xticks(fontsize=12)

# Set the font size of y-axis numbers
plt.yticks(fontsize=12)

# Annotate each point with its coordinates
for i, (x, y) in enumerate(zip(x_values, kw)):
    plt.annotate(f'({x}, {y:.3f})', (x, y), textcoords="offset points", xytext=(0, 10), ha='left', fontsize=12)

# Add legend
plt.legend(fontsize=15)

# Display the plot
plt.show()
