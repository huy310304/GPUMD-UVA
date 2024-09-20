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

shc_nu_list = [shc_nu_1, shc_nu_2, shc_nu_3, shc_nu_4, shc_nu_5]

shc_kw_1 = np.load("shc_kw_1_400_file.npy")
shc_kw_2 = np.load("shc_kw_2_400_file.npy")
shc_kw_3 = np.load("shc_kw_3_400_file.npy")
shc_kw_4 = np.load("shc_kw_4_400_file.npy")
shc_kw_5 = np.load("shc_kw_5_400_file.npy")

shc_kw_list = [shc_kw_1, shc_kw_2, shc_kw_3, shc_kw_4, shc_kw_5]

length = len(shc_kw_list)

shc_nu_avg = (shc_nu_1 + shc_nu_2 + shc_nu_3 + shc_nu_4 + shc_nu_5) / length

shc_kw_avg = (shc_kw_1 + shc_kw_2 + shc_kw_3 + shc_kw_4 + shc_kw_5) / length

## Save the output avg file in .npy
np.save("shc_nu_avg_100K_Optimized_F", shc_nu_avg)
np.save("shc_kw_avg_100K_Optimized_F", shc_kw_avg)

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


# Load the data
kappa_1 = np.load("kappa_1_file.npy", allow_pickle=True).item()  # Treat as dictionary
kappa_2 = np.load("kappa_2_file.npy", allow_pickle=True).item()
kappa_3 = np.load("kappa_3_file.npy", allow_pickle=True).item()
kappa_4 = np.load("kappa_4_file.npy", allow_pickle=True).item()
kappa_5 = np.load("kappa_5_file.npy", allow_pickle=True).item()

# Time arrays for each kappa file
t_1 = np.arange(1, len(kappa_1['kxi']) + 1) * 0.001  # ns
t_2 = np.arange(1, len(kappa_2['kxi']) + 1) * 0.001  # ns
t_3 = np.arange(1, len(kappa_3['kxi']) + 1) * 0.001  # ns
t_4 = np.arange(1, len(kappa_4['kxi']) + 1) * 0.001  # ns
t_5 = np.arange(1, len(kappa_5['kxi']) + 1) * 0.001  # ns


# Update dictionary with running averages
kappa_1['kyi_ra'] = running_ave(kappa_1['kyi'], t_1)
kappa_1['kyo_ra'] = running_ave(kappa_1['kyo'], t_1)
kappa_1['kxi_ra'] = running_ave(kappa_1['kxi'], t_1)
kappa_1['kxo_ra'] = running_ave(kappa_1['kxo'], t_1)
kappa_1['kz_ra'] = running_ave(kappa_1['kz'], t_1)


# Calculate running averages and update dictionaries for kappa_2
kappa_2['kyi_ra'] = running_ave(kappa_2['kyi'], t_2)
kappa_2['kyo_ra'] = running_ave(kappa_2['kyo'], t_2)
kappa_2['kxi_ra'] = running_ave(kappa_2['kxi'], t_2)
kappa_2['kxo_ra'] = running_ave(kappa_2['kxo'], t_2)
kappa_2['kz_ra'] = running_ave(kappa_2['kz'], t_2)

# Repeat for kappa_3
kappa_3['kyi_ra'] = running_ave(kappa_3['kyi'], t_3)
kappa_3['kyo_ra'] = running_ave(kappa_3['kyo'], t_3)
kappa_3['kxi_ra'] = running_ave(kappa_3['kxi'], t_3)
kappa_3['kxo_ra'] = running_ave(kappa_3['kxo'], t_3)
kappa_3['kz_ra'] = running_ave(kappa_3['kz'], t_3)

# Repeat for kappa_4
kappa_4['kyi_ra'] = running_ave(kappa_4['kyi'], t_4)
kappa_4['kyo_ra'] = running_ave(kappa_4['kyo'], t_4)
kappa_4['kxi_ra'] = running_ave(kappa_4['kxi'], t_4)
kappa_4['kxo_ra'] = running_ave(kappa_4['kxo'], t_4)
kappa_4['kz_ra'] = running_ave(kappa_4['kz'], t_4)

# Repeat for kappa_5
kappa_5['kyi_ra'] = running_ave(kappa_5['kyi'], t_5)
kappa_5['kyo_ra'] = running_ave(kappa_5['kyo'], t_5)
kappa_5['kxi_ra'] = running_ave(kappa_5['kxi'], t_5)
kappa_5['kxo_ra'] = running_ave(kappa_5['kxo'], t_5)
kappa_5['kz_ra'] = running_ave(kappa_5['kz'], t_5)


# Aggregate data
all_kyi_ra = [kappa_1['kyi_ra'], kappa_2['kyi_ra'], kappa_3['kyi_ra'], kappa_4['kyi_ra'], kappa_5['kyi_ra']]
all_kyo_ra = [kappa_1['kyo_ra'], kappa_2['kyo_ra'], kappa_3['kyo_ra'], kappa_4['kyo_ra'], kappa_5['kyo_ra']]
all_kxi_ra = [kappa_1['kxi_ra'], kappa_2['kxi_ra'], kappa_3['kxi_ra'], kappa_4['kxi_ra'], kappa_5['kxi_ra']]
all_kxo_ra = [kappa_1['kxo_ra'], kappa_2['kxo_ra'], kappa_3['kxo_ra'], kappa_4['kxo_ra'], kappa_5['kxo_ra']]
all_kz_ra  = [kappa_1['kz_ra'], kappa_2['kz_ra'], kappa_3['kz_ra'], kappa_4['kz_ra'], kappa_5['kz_ra']]

# Compute the mean for each component
mean_kyi_ra = np.mean(all_kyi_ra, axis=0)
mean_kyo_ra = np.mean(all_kyo_ra, axis=0)
mean_kxi_ra = np.mean(all_kxi_ra, axis=0)
mean_kxo_ra = np.mean(all_kxo_ra, axis=0)
mean_kz_ra = np.mean(all_kz_ra, axis=0)

print(len(kappa_1['kxi']), len(kappa_2['kxi']), len(kappa_3['kxi']), len(kappa_4['kxi']), len(kappa_5['kxi']))



# Plot thermal conductivity

plt.figure(figsize=(12, 10))

# Subplot for kyi_ra
plt.subplot(2, 2, 1)
plt.plot(t, kappa_1['kyi_ra'], linewidth=2, label="run1")
plt.plot(t, kappa_2['kyi_ra'], linewidth=2, label="run2")
plt.plot(t, kappa_3['kyi_ra'], linewidth=2, label="run3")
plt.plot(t, kappa_4['kyi_ra'], linewidth=2, label="run4")
plt.plot(t, kappa_5['kyi_ra'], linewidth=2, label="run5")
plt.plot(t, mean_kyi_ra, linewidth=4, label="Average", color="red")
plt.legend(fontsize="small")
plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{in}$ W/m/K')
plt.title('(a)')

# Subplot for kyo_ra
plt.subplot(2, 2, 2)
plt.plot(t, kappa_1['kyo_ra'], linewidth=2, label="run1")
plt.plot(t, kappa_2['kyo_ra'], linewidth=2, label="run2")
plt.plot(t, kappa_3['kyo_ra'], linewidth=2, label="run3")
plt.plot(t, kappa_4['kyo_ra'], linewidth=2, label="run4")
plt.plot(t, kappa_5['kyo_ra'], linewidth=2, label="run5")
plt.plot(t, mean_kyo_ra, linewidth=4, label="Average", color="red")
plt.legend(fontsize="small")
plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{out}$ (W/m/K)')
plt.title('(b)')

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