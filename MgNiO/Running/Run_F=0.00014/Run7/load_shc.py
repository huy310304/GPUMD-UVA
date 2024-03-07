# Plot spectral heat current results

from pylab import *
from gpyumd.atoms import GpumdAtoms
from ase.io import write
from ase.io import read
from gpyumd.load import load_shc, load_kappa
from gpyumd.math import running_ave
from gpyumd.calc import calc_spectral_kappa
import numpy as np

shc = load_shc(num_corr_points=250, num_omega=400)['run0'] # 400 pts
shc.keys()

l = [42.241998216000006, 42.241998216000006, 42.241998216000006] # Change size if needed
Lx, Lz = l[0], l[2]
Ly = 4.2241998216000006 # Change size if needed
V = Lx * Ly * Lz
T = 300
Fe = 1.4e-4 # Change Force if needed
calc_spectral_kappa(shc, driving_force=Fe, temperature=T, volume=V)
shc['kw'] = shc['kwi'] + shc['kwo']
shc['K'] = shc['Ki'] + shc['Ko']
shc.keys()

shc_nu_1 = shc['nu']
shc_kw_1 = shc['kw']
np.save("shc_nu_7_400_file", shc_nu_1)
np.save("shc_kw_7_400_file", shc_kw_1)
