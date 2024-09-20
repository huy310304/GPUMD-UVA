from pylab import *
from ase.lattice.cubic import Diamond
from ase.io import write
from gpyumd.load import load_thermo
import matplotlib.pyplot as plt

thermo = load_thermo()
print("Thermo quantities:", list(thermo.keys()))

# print out the box shape afterward
print(thermo["Lx"], thermo["Ly"], thermo["Lz"])

kinetic_energy= thermo["K"]
potential_energy = thermo["U"]
pressure_x = thermo["Px"]
pressure_y = thermo["Py"]
pressure_z = thermo["Pz"]

plt.plot(kinetic_energy)
plt.plot(potential_energy)
plt.show()


plt.plot(pressure_x, label="Px")
plt.plot(pressure_y, label="Py")
plt.plot(pressure_z, label="Pz")
plt.title("Pressure Using Relaxed Volume From NPT Run")
plt.legend()
plt.show()


