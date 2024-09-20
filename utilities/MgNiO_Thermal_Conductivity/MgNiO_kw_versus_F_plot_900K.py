import matplotlib.pyplot as plt
from math import sqrt

# Sample data for the line
x_values = [0, 0.00045]
y_value = 3.3

# # Plot the straight line
# plt.plot(x_values, [y_value, y_value], color="green", label=f'k(w) = {y_value}')

# Data for the points
F_values = [0.00014, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006]
kw = [3.293, 3.334, 3.362, 3.538, 3.538, 4.230] # Avg values


# # Data for the standard deviation
# std_dev = [1.8506, 0.3666, 0.2891, 0.1114, 0.0966, 0.3387, 0.1487]

# Data for error of the mean
errors = [0.099, 0.070, 0.097, 0.012, 0.045, 0.171]

# Plot the points with "x" marks
plt.errorbar(F_values, kw, yerr=errors, fmt='x', markersize=7, color='red', label='Points')

# # Plot the stdev bars with different color
# plt.errorbar(F_values, kw, yerr=std_dev, fmt='none', ecolor='blue', label='Standard Deviation')

# Plot the error bars with different color
plt.errorbar(F_values, kw, yerr=errors, fmt='none', ecolor='orange', label='Error Bars')

# Add labels and title
plt.xlabel('F-values', fontsize=20)
plt.ylabel('k(w) using integration', fontsize=20)
plt.title('Temp 900K - K(w) versus F-values', fontsize = 20)
plt.xlim(0.0001, 0.00065)
plt.ylim(3, 4.5)

# Set the font size of x-axis numbers
plt.xticks(fontsize=12)

# Set the font size of x-axis numbers
plt.yticks(fontsize=12)

# Annotate each point with its coordinates
for i, (x, y) in enumerate(zip(F_values, kw)):
    plt.annotate(f'({x}, {y:.3f})', (x, y), textcoords="offset points", xytext=(0,10), ha='left', fontsize=10)

# Add legend
plt.legend(fontsize = 15, loc = 2)

# Display the plot
plt.show()
