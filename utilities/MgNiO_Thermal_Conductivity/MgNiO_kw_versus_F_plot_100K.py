import matplotlib.pyplot as plt
from math import sqrt

# Sample data for the line
x_values = [0, 0.00045]
y_value = 3.3

# Plot the straight line
# plt.plot(x_values, [y_value, y_value], color="green", label=f'k(w) = {y_value}')

# Data for the points
F_values = [0.000035, 0.00005, 0.00007, 0.00009, 0.00010, 0.00011, 0.00014]
kw = [4.169, 4.968, 4.428, 5.089, 4.968, 5.711, 5.799] # Avg values


# # Data for the standard deviation
# std_dev = [1.8506, 0.3666, 0.2891, 0.1114, 0.0966, 0.3387, 0.1487]

# Data for error of the mean
errors = [0.326, 0.295,	0.318, 0.180, 0.111, 0.2099, 0.240]

# Plot the points with "x" marks
plt.errorbar(F_values, kw, yerr=errors, fmt='x', markersize=7, color='red', label='Points')

# # Plot the stdev bars with different color
# plt.errorbar(F_values, kw, yerr=std_dev, fmt='none', ecolor='blue', label='Standard Deviation')

# Plot the error bars with different color
plt.errorbar(F_values, kw, yerr=errors, fmt='none', ecolor='orange', label='Error Bars')

# Add labels and title
plt.xlabel('F-values', fontsize=20)
plt.ylabel('k(w) using integration', fontsize=20)
plt.title('Temp 100K - K(w) versus F-values', fontsize = 20)
plt.xlim(0.00003, 0.00015)
plt.ylim(3.8, 6.2)

# Set the font size of x-axis numbers
plt.xticks(fontsize=12)

# Set the font size of x-axis numbers
plt.yticks(fontsize=12)

# Annotate each point with its coordinates
for i, (x, y) in enumerate(zip(F_values, kw)):
    plt.annotate(f'({x}, {y:.3f})', (x, y), textcoords="offset points", xytext=(0,10), ha='left', fontsize=10)

# Add legend
plt.legend(fontsize = 15, loc=2)

# Display the plot
plt.show()
