from pylab import *
from gpyumd.atoms import GpumdAtoms
from ase.io import write
from ase.io import read
from gpyumd.load import load_shc, load_kappa
from gpyumd.math import running_ave
from gpyumd.calc import calc_spectral_kappa
import numpy as np

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

## Save Kappa data
np.save("kappa_2_file", kappa)


# Plot thermal conductivity

figure(figsize=(12,10))
subplot(2,2,1)
set_fig_properties([gca()])
#plot(t, kappa['kyi'],color='C7',alpha=0.5)
plot(t, kappa['kyi_ra'], linewidth=2)
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
ylim([-12, 12])
#gca().set_yticks(range(-2000,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa_{in}$ W/m/K')
title('(a)')

subplot(2,2,2)
set_fig_properties([gca()])
#plot(t, kappa['kyo'],color='C7',alpha=0.5)
plot(t, kappa['kyo_ra'], linewidth=2, color='C3')
#xlim([0, 10])
#gca().set_xticks(range(0,11,2))
ylim([-12, 12])
#gca().set_yticks(range(0,4001,1000))
xlabel('time (ns)')
ylabel(r'$\kappa_{out}$ (W/m/K)')
title('(b)')

subplot(2,2,3)
set_fig_properties([gca()])
plot(t, kappa['kyi_ra'], linewidth=2)
plot(t, kappa['kyo_ra'], linewidth=2, color='C3')
plot(t, kappa['kyi_ra']+kappa['kyo_ra'], linewidth=2, color='k')
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
plot(t, kappa['kyi_ra']+kappa['kyo_ra'],color='k', linewidth=2)
plot(t, kappa['kxi_ra']+kappa['kxo_ra'], color='C0', linewidth=2)
plot(t, kappa['kz_ra'], color='C3', linewidth=2)
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

shc = load_shc(num_corr_points=250, num_omega=400)['run0']
shc.keys()

l = [42.73557981, 42.73557981, 42.73557981]
Lx, Lz = l[0], l[2]
Ly = 4.273557981
V = Lx * Ly * Lz

T = 900 # Change Temp to 100K here
Fe = 4e-4 # Change Force to 1.4e-4 here

calc_spectral_kappa(shc, driving_force=Fe, temperature=T, volume=V)
shc['kw'] = shc['kwi'] + shc['kwo']
shc['K'] = shc['Ki'] + shc['Ko']
Gc = np.load('../../../ballistic/Run3/Gc_400.npy')
shc.keys()




# Save shc stuff for plotting AVG TC
shc_nu = shc['nu']
shc_kw = shc['kw']
np.save("shc_nu_2_400_file", shc_nu)
np.save("shc_kw_2_400_file", shc_kw)




lambda_i = shc['kw']/Gc
length = np.logspace(1,6,100)
k_L = np.zeros_like(length)
for i, el in enumerate(length):
    k_L[i] = np.trapz(shc['kw']/(1+lambda_i/el), shc['nu'])

figure(figsize=(12,10))
subplot(2,2,1)
set_fig_properties([gca()])
plot(shc['t'], shc['K']/Ly, linewidth=3)
#xlim([-0.5, 0.5])
#gca().set_xticks([-0.5, 0, 0.5])
#ylim([-12, 12])
#gca().set_yticks(range(-1,6,1))
ylabel('K (eV/ps)')
xlabel('Correlation time (ps)')
title('(a)')

subplot(2,2,2)
set_fig_properties([gca()])
plot(shc['nu'], shc['kw'],linewidth=3)
#xlim([0, 50])
#gca().set_xticks(range(0,51,10))
ylim([-0.2, 1])
#gca().set_yticks(range(0,201,50))
ylabel(r'$\kappa$($\omega$) (W/m/K/THz)')
xlabel(r'$\nu$ (THz)')
title('(b)')
subplot(2,2,3)
set_fig_properties([gca()])
plot(shc['nu'], lambda_i,linewidth=3)
#xlim([0, 50])
#gca().set_xticks(range(0,51,10))
#ylim([0, 6000])
#gca().set_yticks(range(0,6001,1000))
ylabel(r'$\lambda$($\omega$) (nm)')
xlabel(r'$\nu$ (THz)')
title('(c)')

subplot(2,2,4)
set_fig_properties([gca()])
semilogx(length/1000, k_L,linewidth=3)
#xlim([1e-2, 1e3])
#ylim([0, 3000])
#gca().set_yticks(range(0,3001,500))
ylabel(r'$\kappa$ (W/m/K)')
xlabel(r'L ($\mu$m)')
title('(d)')

tight_layout()
show()

