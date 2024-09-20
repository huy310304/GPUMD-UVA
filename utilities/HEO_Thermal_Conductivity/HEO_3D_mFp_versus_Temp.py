import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data
lambda_i_avg_900K = np.load("lambda_i_avg_900K_Optimized_F.npy")
lambda_i_avg_700K = np.load("lambda_i_avg_700K_Optimized_F.npy")
lambda_i_avg_500K = np.load("lambda_i_avg_500K_Optimized_F.npy")
lambda_i_avg_300K = np.load("lambda_i_avg_300K_Optimized_F.npy")
# lambda_i_avg_100K = np.load("lambda_i_avg_100K_Optimized_F.npy")
shc_nu = np.load("shc_nu_avg_300K_Optimized_F.npy")

# Slice arrays to include only the first 280 data point to cut the part that Gc or k(w) go to 0
start = 0
num_points = 250
x_values = np.array([300, 500, 700, 900])  # 4 different Temps
y_values_per_x = [shc_nu[start:num_points], shc_nu[start:num_points], shc_nu[start:num_points], shc_nu[start:num_points]]
z_values_per_x = [lambda_i_avg_300K[start:num_points], lambda_i_avg_500K[start:num_points], lambda_i_avg_700K[start:num_points], lambda_i_avg_900K[start:num_points]]

# Create the figure
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface for each x value with thicker lines
for i, x_val in enumerate(x_values):
    ax.plot(np.full(num_points - start, x_val), y_values_per_x[i], z_values_per_x[i], label=f'Temp={x_val}K', linewidth=3.0)

ax.set_xlabel('Temp (K)')
ax.set_ylabel('nu (THz)')
ax.set_zlabel(r'$\lambda$($\omega$) (nm)')
ax.set_title(r'$\lambda$($\omega$) (nm) versus $\nu$ (THz) with different Temp (K)')

ax.legend()

plt.show()