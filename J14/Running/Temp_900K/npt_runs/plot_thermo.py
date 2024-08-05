from pylab import *
from ase.lattice.cubic import Diamond
from ase.io import write
from gpyumd.load import load_thermo

thermo = load_thermo()
print("Thermo quantities:", list(thermo.keys()))

# print out the box shape afterward
print(thermo["Lx"], thermo["Ly"], thermo["Lz"])
print(len(thermo["Lx"]), thermo["Lx"])
