from pylab import *
from gpyumd.atoms import GpumdAtoms
from ase.io import write
from ase.io import read
from gpyumd.load import load_shc, load_kappa
from gpyumd.math import running_ave
from gpyumd.calc import calc_spectral_kappa
import numpy as np
import matplotlib.pyplot as plt

shc_nu_1 = np.load("shc_nu_1_400_file.npy")
shc_nu_2 = np.load("shc_nu_2_400_file.npy")
shc_nu_3 = np.load("shc_nu_3_400_file.npy")
shc_nu_4 = np.load("shc_nu_4_400_file.npy")
shc_nu_5 = np.load("shc_nu_5_400_file.npy")
shc_nu_6 = np.load("shc_nu_6_400_file.npy")
shc_nu_7 = np.load("shc_nu_7_400_file.npy")
shc_nu_8 = np.load("shc_nu_8_400_file.npy")
shc_nu_9 = np.load("shc_nu_9_400_file.npy")
shc_nu_10 = np.load("shc_nu_10_400_file.npy")

shc_nu_list = [shc_nu_1, shc_nu_2, shc_nu_3, shc_nu_4, shc_nu_5, shc_nu_6, shc_nu_7, shc_nu_8, shc_nu_9, shc_nu_10]

shc_kw_1 = np.load("shc_kw_1_400_file.npy")
shc_kw_2 = np.load("shc_kw_2_400_file.npy")
shc_kw_3 = np.load("shc_kw_3_400_file.npy")
shc_kw_4 = np.load("shc_kw_4_400_file.npy")
shc_kw_5 = np.load("shc_kw_5_400_file.npy")
shc_kw_6 = np.load("shc_kw_6_400_file.npy")
shc_kw_7 = np.load("shc_kw_7_400_file.npy")
shc_kw_8 = np.load("shc_kw_8_400_file.npy")
shc_kw_9 = np.load("shc_kw_9_400_file.npy")
shc_kw_10 = np.load("shc_kw_10_400_file.npy")

shc_kw_list = [shc_kw_1, shc_kw_2, shc_kw_3, shc_kw_4, shc_kw_5, shc_kw_6, shc_kw_7, shc_kw_8, shc_kw_9, shc_kw_10]

shc_nu_avg = (shc_nu_1 + shc_nu_2 + shc_nu_3 + shc_nu_4 + shc_nu_5 + shc_nu_6 + shc_nu_7 + shc_nu_8 + shc_nu_9 + shc_nu_10) / 10

shc_kw_avg = (shc_kw_1 + shc_kw_2 + shc_kw_3 + shc_kw_4 + shc_kw_5 + shc_kw_6 + shc_kw_7 + shc_kw_8 + shc_kw_9 + shc_kw_10) / 10

# Save the output avg file in .npy
np.save("shc_nu_avg_300K", shc_nu_avg)
np.save("shc_kw_avg_300K", shc_kw_avg)


# Integral using Riemann Sum
total = 0
for shc_nu, shc_kw in zip(shc_nu_list, shc_kw_list): 
  dx = (max(shc_nu) - min(shc_nu)) / 400
  sum = 0
  for shc_kw_value in shc_kw:
    sum += shc_kw_value*dx
  total += sum
  print(f"Riemann Sum: {sum:.6f}") 

avg = total / 10
print(f"Average Integral Value: {avg}")

print()
  
# Mean of each k(w) 
#for shc_kw in shc_kw_list:
#  mean = np.mean(shc_kw)
#  print(f"Mean of kw: {mean:.6f}")

#print()

# Standard deviation of each k(w)
#for shc_kw in shc_kw_list:
#  std = np.std(shc_kw)
#  print(f"Standard dev of kw: {std:.6f}")
  

aw = 2
fs = 16
font = {'size'   : fs}
matplotlib.rc('font', **font)
matplotlib.rc('axes' , linewidth=aw)

def set_fig_properties(ax_list):
    tl = 8
    tw = 2
    tlm = 4

    for ax in ax_list:
        ax.tick_params(which='major', length=tl, width=tw)
        ax.tick_params(which='minor', length=tlm, width=tw)
        ax.tick_params(which='both', axis='both', direction='in', right=True, top=True)

kappa = load_kappa()
kappa.keys()

t = np.arange(1,kappa['kxi'].shape[0]+1)*0.001  # ns
kappa['kyi_ra'] = running_ave(kappa['kyi'],t)
kappa['kyo_ra'] = running_ave(kappa['kyo'],t)
kappa['kxi_ra'] = running_ave(kappa['kxi'],t)
kappa['kxo_ra'] = running_ave(kappa['kxo'],t)
kappa['kz_ra'] = running_ave(kappa['kz'],t)

# Load data for all kappa datasets
kappas = []
for i in range(1, 6):
    kappa = np.load(f"kappa_{i}_file.npy", allow_pickle=True).item()
    kappas.append(kappa)

# Assuming all kappa files have the same number of time points
t = np.arange(1, len(kappas[0]['kxi']) + 1) * 0.001  # ns

# Compute running averages for each kappa
for kappa in kappas:
    kappa['kyi_ra'] = running_ave(kappa['kyi'], t)
    kappa['kyo_ra'] = running_ave(kappa['kyo'], t)
    kappa['kxi_ra'] = running_ave(kappa['kxi'], t)
    kappa['kxo_ra'] = running_ave(kappa['kxo'], t)
    kappa['kz_ra'] = running_ave(kappa['kz'], t)

# Aggregate data
all_kyi_ra = [kappa['kyi_ra'] for kappa in kappas]
all_kyo_ra = [kappa['kyo_ra'] for kappa in kappas]
all_kxi_ra = [kappa['kxi_ra'] for kappa in kappas]
all_kxo_ra = [kappa['kxo_ra'] for kappa in kappas]
all_kz_ra  = [kappa['kz_ra'] for kappa in kappas]

# Compute the mean for each component
mean_kyi_ra = np.mean(all_kyi_ra, axis=0)
mean_kyo_ra = np.mean(all_kyo_ra, axis=0)
mean_kxi_ra = np.mean(all_kxi_ra, axis=0)
mean_kxo_ra = np.mean(all_kxo_ra, axis=0)
mean_kz_ra = np.mean(all_kz_ra, axis=0)


# Plot thermal conductivity

# Plot thermal conductivity for in-plane 'kyi'
plt.figure(figsize=(12, 10))
plt.subplot(2, 2, 1)
for i, kappa in enumerate(kappas, start=1):
    plt.plot(t, kappa['kyi_ra'], linewidth=2, label=f"run{i}")
plt.plot(t, mean_kyi_ra, linewidth=4, label="Average", color="red")
plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{in}$ W/m/K')
plt.title('(a) In-plane')

# Plot thermal conductivity for out-of-plane 'kyo'
plt.subplot(2, 2, 2)
for i, kappa in enumerate(kappas, start=1):
    plt.plot(t, kappa['kyo_ra'], linewidth=2, label=f"run{i}")
plt.plot(t, mean_kyo_ra, linewidth=4, label="Average", color="red")
plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{out}$ W/m/K')
plt.title('(b) Out-of-plane')


figure(figsize=(12,10))
subplot(2,2,1)
set_fig_properties([gca()])
#plot(t, kappa['kyi'],color='C7',alpha=0.5)
plot(t, mean_kyi_ra, linewidth=2)
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
#ylim([-12, 12])
#gca().set_yticks(range(-2000,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa_{in}$ W/m/K')
title('(a)')

subplot(2,2,2)
set_fig_properties([gca()])
#plot(t, kappa['kyo'],color='C7',alpha=0.5)
plot(t, mean_kyo_ra, linewidth=2, color='C3')
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
#ylim([-12, 12])
#gca().set_yticks(range(0,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa_{out}$ (W/m/K)')
title('(b)')

subplot(2,2,3)
set_fig_properties([gca()])
plot(t, mean_kyi_ra, linewidth=2)
plot(t, mean_kyo_ra, linewidth=2, color='C3')
plot(t, mean_kyi_ra + mean_kyo_ra, linewidth=2, color='k')
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
#ylim([0, 4000])
#gca().set_yticks(range(0,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa$ (W/m/K)')
legend(['in', 'out', 'total'])
title('(c)')


subplot(2,2,4)
set_fig_properties([gca()])
plot(t, mean_kyi_ra + mean_kyo_ra,color='k', linewidth=2)
plot(t, mean_kxi_ra + mean_kxo_ra, color='C0', linewidth=2)
plot(t, mean_kz_ra, color='C3', linewidth=2)
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
#ylim([0, 4000])
#gca().set_yticks(range(-2000,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa$ (W/m/K)')
legend(['yy', 'xy', 'zy'])
title('(d)')

tight_layout()
show()