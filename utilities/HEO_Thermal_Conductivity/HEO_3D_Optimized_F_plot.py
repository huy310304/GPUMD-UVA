import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load sample data
shc_kw_avg_900K = np.load("shc_kw_avg_900K_Optimized_F.npy")
shc_nu_avg_900K = np.load("shc_nu_avg_900K_Optimized_F.npy")
shc_kw_avg_700K = np.load("shc_kw_avg_700K_Optimized_F.npy")
shc_nu_avg_700K = np.load("shc_nu_avg_700K_Optimized_F.npy")
shc_kw_avg_500K = np.load("shc_kw_avg_500K_Optimized_F.npy")
shc_nu_avg_500K = np.load("shc_nu_avg_500K_Optimized_F.npy")
shc_kw_avg_300K = np.load("shc_kw_avg_300K_Optimized_F.npy")
shc_nu_avg_300K = np.load("shc_nu_avg_300K_Optimized_F.npy")
# shc_kw_avg_100K = np.load("shc_kw_avg_100K_Optimized_F.npy")
# shc_nu_avg_100K = np.load("shc_nu_avg_100K_Optimized_F.npy")

num_points = 400
x_values = np.array([300, 500, 700, 900])  # 5 distinct x values
y_values_per_x = [shc_nu_avg_300K, shc_nu_avg_500K, shc_nu_avg_700K, shc_nu_avg_900K]
z_values_per_x = [shc_kw_avg_300K, shc_kw_avg_500K, shc_kw_avg_700K, shc_kw_avg_900K]

# Create a larger figurec
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface for each x value with thicker lines
for i, x_val in enumerate(x_values):
    ax.plot(np.full(num_points, x_val), y_values_per_x[i], z_values_per_x[i], label=f'Temp={x_val}K', linewidth=3.0)

# Add labels and title
ax.set_xlabel('Temp (K)')
ax.set_ylabel('nu (THz)')
ax.set_zlabel('k(W)')
ax.set_title("3D Plot using Optimized F")

# Add legend
ax.legend()

# Show plot
plt.show()