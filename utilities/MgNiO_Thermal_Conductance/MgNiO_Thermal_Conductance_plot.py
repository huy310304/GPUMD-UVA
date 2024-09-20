import matplotlib.pyplot as plt
import numpy as np

Gc_100K = np.load("Gc_100K.npy")
Gc_300K = np.load("Gc_300K.npy")
Gc_500K = np.load("Gc_500K.npy")
Gc_700K = np.load("Gc_700K.npy")
Gc_900K = np.load("Gc_900K.npy")

shc_nu = np.load("../MgNiO_Thermal_Conductivity/shc_nu_avg_100K_Optimized_F.npy")


# Replace to plot all Thermal Conductance at different temparature

plt.plot(shc_nu, Gc_900K, linewidth=2)
plt.xlim([0, 25])
#gca().set_xticks(range(0,51,10))
plt.ylim([0, 0.10])
#gca().set_yticks(linspace(0,0.35,8))
plt.ylabel(r'$G$($\omega$) (GW/m$^2$/K/THz)')
plt.xlabel(r'$\omega$/2$\pi$ (THz)')
plt.title('Thermal Conductance vs Frequency')
plt.tight_layout()
plt.show()