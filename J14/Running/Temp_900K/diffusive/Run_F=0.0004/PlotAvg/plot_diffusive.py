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
np.save("shc_nu_avg_900K_Optimized_F", shc_nu_avg)
np.save("shc_kw_avg_900K_Optimized_F", shc_kw_avg)

# Integral using Riemann Sum
total = 0
for shc_nu, shc_kw in zip(shc_nu_list, shc_kw_list): 
  dx = (max(shc_nu) - min(shc_nu)) / 400
  sum = 0
  for shc_kw_value in shc_kw:
    sum += shc_kw_value*dx
  total += sum
  print(f"Riemann Sum: {sum:.6f}") 

avg = total / length
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

# kappa = load_kappa()
# kappa.keys()

# t = np.arange(1,kappa['kxi'].shape[0]+1)*0.001  # ns
# kappa['kyi_ra'] = running_ave(kappa['kyi'],t)
# kappa['kyo_ra'] = running_ave(kappa['kyo'],t)
# kappa['kxi_ra'] = running_ave(kappa['kxi'],t)
# kappa['kxo_ra'] = running_ave(kappa['kxo'],t)
# kappa['kz_ra'] = running_ave(kappa['kz'],t)

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
#plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{in}$ W/m/K')
plt.title('(a) In-plane')

# Plot thermal conductivity for out-of-plane 'kyo'
plt.subplot(2, 2, 2)
for i, kappa in enumerate(kappas, start=1):
    plt.plot(t, kappa['kyo_ra'], linewidth=2, label=f"run{i}")
plt.plot(t, mean_kyo_ra, linewidth=4, label="Average", color="red")
#plt.ylim([-12, 12])
plt.xlabel('time (ns)')
plt.ylabel(r'$\kappa_{out}$ W/m/K')
plt.title('(b) Out-of-plane')


#subplot(2,2,1)
#set_fig_properties([gca()])
##plot(t, kappa['kyi'],color='C7',alpha=0.5)
#plot(t, mean_kyi_ra, linewidth=2)
##xlim([0, 10])
##gca().set_xticks(range(0,11,2))
##ylim([-12, 12])
##gca().set_yticks(range(-2000,4001,1000))
#xlabel('time (ns)')
#ylabel(r'$\kappa_{in}$ W/m/K')
#title('(a)')
#
#subplot(2,2,2)
#set_fig_properties([gca()])
##plot(t, kappa['kyo'],color='C7',alpha=0.5)
#plot(t, mean_kyo_ra, linewidth=2, color='C3')
##xlim([0, 10])
##gca().set_xticks(range(0,11,2))
##ylim([-12, 12])
##gca().set_yticks(range(0,4001,1000))
#xlabel('time (ns)')
#ylabel(r'$\kappa_{out}$ (W/m/K)')
#title('(b)')

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
plot(t, mean_kyi_ra + mean_kyo_ra, color='k', linewidth=2)
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

# Plot spectral heat current results

# shc = load_shc(num_corr_points=250, num_omega=400)['run0'] #CHANGE NUMBERS OF POINTS HERE
# shc.keys()

#l = [42.241998216000006, 42.241998216000006, 42.241998216000006]
#Lx, Lz = l[0], l[2]
#Ly = 4.2241998216000006
#V = Lx * Ly * Lz
#T = 300 # change force here 
#Fe = 1.4e-4 # change temp here
#calc_spectral_kappa(shc, driving_force=Fe, temperature=T, volume=V)
#shc['kw'] = shc['kwi'] + shc['kwo']
#shc['K'] = shc['Ki'] + shc['Ko']

# xai sai Gc sai subplot 2,2,3 ma th ke me, minh chi lay cai final 2,2,2 thoi
Gc = np.load('../../../ballistic/Run3/Gc_400.npy') #CHANGE FILE NAME
#shc.keys()

lambda_i_avg = shc_kw_avg / Gc
length = np.logspace(1,6,100)
k_L = np.zeros_like(length)
for i, el in enumerate(length):
    k_L[i] = np.trapz(shc_kw_avg/(1+lambda_i_avg/el), shc_nu_avg)
    
    
# Save avg optimized lambda_i
np.save("lambda_i_avg_900K_Optimized_F", lambda_i_avg)


#figure(figsize=(12,10))
#subplot(2,2,1)
#set_fig_properties([gca()])
#plot(shc['t'], shc['K']/Ly, linewidth=3)
##xlim([-0.5, 0.5])
##gca().set_xticks([-0.5, 0, 0.5])
##ylim([-12, 12])
##gca().set_yticks(range(-1,6,1))
#ylabel('K (eV/ps)')
#xlabel('Correlation time (ps)')
#title('(a)')


# AVG PLOT for log(lambda) vs log(frequency)
subplot(2,2,1)
loglog(shc_nu_avg[:300], lambda_i_avg[:300], linewidth=3)  # Use semilogx for log-linear scale
ylabel(r'$\lambda$($\omega$) (nm)')
xlabel(r'$\nu$ (THz)')
title('(c) log(lambda) versus log(frequency)')


subplot(2,2,2)
set_fig_properties([gca()])
plot(shc_nu_avg, shc_kw_avg,linewidth=3)
xlim([-1, 18]) # Set x_limit to 18 THz to ignore the G(w) behavior
#gca().set_xticks(range(0,51,10))
# ylim([-0.1, 0.8])
#gca().set_yticks(range(0,201,50))
ylabel(r'$\kappa$($\omega$) (W/m/K/THz)')
xlabel(r'$\nu$ (THz)')
title('(b)')

# AVG PLOT for lambda vs frequency
subplot(2,2,3)
set_fig_properties([gca()])
plot(shc_nu_avg[:300], lambda_i_avg[:300], linewidth=3)
#xlim([0, 50])
#gca().set_xticks(range(0,51,10))
#ylim([0, 6000])
#gca().set_yticks(range(0,6001,1000))
ylabel(r'$\lambda$($\omega$) (nm)')
xlabel(r'$\nu$ (THz)')
title('(c) lambda vs frequency')


# AVG PLOT for lambda vs log(frequency)
subplot(2,2,4)
semilogx(shc_nu_avg[:300], lambda_i_avg[:300], linewidth=3)  # Use semilogx for log-linear scale
ylabel(r'$\lambda$($\omega$) (nm)')
xlabel(r'$\nu$ (THz)')
title('(c) lambda vs log(frequency)')

tight_layout()
show()

subplot(2,2,4)
set_fig_properties([gca()])
semilogx(length/1000, k_L,linewidth=3)
##xlim([1e-2, 1e3])
##ylim([0, 3000])
##gca().set_yticks(range(0,3001,500))
ylabel(r'$\kappa$ (W/m/K)')
xlabel(r'L ($\mu$m)')
title('(d)')

tight_layout()
show()

# Plot Individual runs
plt.plot(shc_nu_1, shc_kw_1, label = "run1")
plt.plot(shc_nu_2, shc_kw_2, label = "run2")
plt.plot(shc_nu_3, shc_kw_3, label = "run3")
plt.plot(shc_nu_4, shc_kw_4, label = "run4")
plt.plot(shc_nu_5, shc_kw_5, label = "run5")


# Plot the avg run
plt.plot(shc_nu_avg, shc_kw_avg, label = "Avg", linewidth = 4, color = "red")
plt.legend()
ylabel(r'$\kappa$($\omega$) (W/m/K/THz)')
xlabel(r'$\nu$ (THz)')
plt.show()
