import matplotlib.pyplot as plt
import numpy as np

# Original data points
F_values = [0.00022, 0.0004]
Temp = [300, 900]

# Fit a polynomial of degree 1 (line fit)
fit_coeffs = np.polyfit(F_values, Temp, 1)

# Create a polynomial function using the fit coefficients
fit_line = np.poly1d(fit_coeffs)

# Function to calculate F given T using the fit line using T = mF + c
def find_F_for_temp(temp):
    m, c = fit_coeffs
    return (temp - c) / m

# Calculate F for Temp = 500 and Temp = 700
F_for_500 = find_F_for_temp(500)
F_for_700 = find_F_for_temp(700)
F_for_20 = find_F_for_temp(20)

# Points to plot for Temp = 500 and 700
F_fit_values = [F_for_500, F_for_700, F_for_20]
Temp_fit = [500, 700, 20]

# Extend the range of F_values for plotting
extended_F_values_min = min(F_values) - 0.0001  # Extend lower bound
extended_F_values_max = max(F_values)  # Extend upper bound
dense_F_values = np.linspace(extended_F_values_min, extended_F_values_max, 500)

# Calculate the y values for the extended range
fit_values_dense = fit_line(dense_F_values)

# Plot the extended line fit
plt.plot(dense_F_values, fit_values_dense, color='green', linestyle='-', label='Linear Fit')

# Plot the original data points for reference
plt.scatter(F_values, Temp, color='red', label='Original Data')

# Plot the points for Temp = 500 and 700
plt.scatter(F_fit_values, Temp_fit, color='blue', label='Fit Data')



plt.xlabel('F-values', fontsize=20)
plt.ylabel('Temperature', fontsize=20)
plt.title('Extended Temp vs. F-values Straight Line Fit', fontsize=20)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Annotate each original data point
for i, (x, y) in enumerate(zip(F_values, Temp)):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

for i, (x, y) in enumerate(zip(F_fit_values, Temp_fit)):
    plt.annotate(f'({x:.5f}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

plt.legend(fontsize=15)

plt.show()
