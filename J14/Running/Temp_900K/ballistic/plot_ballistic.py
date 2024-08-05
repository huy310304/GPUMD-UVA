from pylab import *
from ase.build import graphene_nanoribbon
from ase.io import write
from gpyumd.atoms import GpumdAtoms
from gpyumd.load import load_shc, load_compute

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
        ax.tick_params(axis='both', direction='in', right=True, top=True)
        
# Every run has different compute.out --> different Gc.npy for each run      
compute = load_compute(['temperature'])
compute.keys()

T = compute['temperature']
Ein = compute['Ein']
Eout = compute['Eout']
ndata = T.shape[0]
temp_ave = mean(T[int(ndata/2)+1:, 1:], axis=0)

dt = 0.001  # ps
Ns = 1000  # Sample interval
t = dt*np.arange(1,ndata+1) * Ns/1000  # ns
figure(figsize=(10,5))
subplot(1,2,1)
set_fig_properties([gca()])
group_idx = range(1,10)
print(group_idx, temp_ave)
plot(group_idx, temp_ave,linewidth=3,marker='o',markersize=10)
#xlim([1, 9])
#gca().set_xticks(group_idx)
#ylim([290, 310])
#gca().set_yticks(range(290,311,5))
xlabel('group index')
ylabel('T (K)')
title('(a)')

subplot(1,2,2)
set_fig_properties([gca()])
plot(t, Ein/1000, 'C3', linewidth=3)
plot(t, Eout/1000, 'C0', linewidth=3, linestyle='--' )
xlim([0, 1])
gca().set_xticks(linspace(0,1,6))
#ylim([-5, 5])
#gca().set_yticks(range(-10,11,5))
xlabel('t (ns)')
ylabel('Heat (keV)')
title('(b)')
tight_layout()
show()


# PLOT SHC
deltaT = temp_ave[0] - temp_ave[-1]  # [K]
print("deltaT:", deltaT)

Q1 = (Ein[int(ndata/2)] - Ein[-1])/(ndata/2)/dt/Ns
Q2 = (Eout[-1] - Eout[int(ndata/2)])/(ndata/2)/dt/Ns
Q = mean([Q1, Q1])  # [eV/ps]
print("Q:", Q)

# l = [lx, ly, lz]
l = [42.73557981, 42.73557981, 42.73557981]
A = l[0]*l[2]/100  # [nm2]
G = 160*Q/deltaT/A  # [GW/m2/K]
print("G:", G)


# Every run has different shc.out --> different Gc.npy for each run

shc = load_shc(250, 400)['run0'] #CHANGE NUMBERS OF POINTS HERE
# Change shc.out file for each F-values
print(shc.keys())

# Ly = split[5]-split[4] # IM NOT SURE HOW TO FIX THIS LINE 
Ly = 4.273557981  #42.73557981 divided by 10
Lx, Lz = l[0], l[2]
V = Lx*Ly*Lz
Gc = 1.6e4*(shc['jwi']+shc['jwo'])/V/deltaT
figure(figsize=(10,5))
subplot(1,2,1)
set_fig_properties([gca()])
plot(shc['t'], (shc['Ki']+shc['Ko'])/Ly, linewidth=2)
#xlim([-0.5, 0.5])
#gca().set_xticks([-0.5, 0, 0.5])
#ylim([-2, 2])
#gca().set_yticks(range(-4,11,2))
ylabel('K (eV/ps)')
xlabel('Correlation time (ps)')
title('(a)')

subplot(1,2,2)
set_fig_properties([gca()])
plot(shc['nu'], Gc, linewidth=2)
#xlim([0, 25])
#gca().set_xticks(range(0,51,10))
#ylim([0, 0.10])
#gca().set_yticks(linspace(0,0.35,8))
ylabel(r'$G$($\omega$) (GW/m$^2$/K/THz)')
xlabel(r'$\omega$/2$\pi$ (THz)')
title('(b)')
tight_layout()
show()

print(Gc)

np.save('Gc_400.npy', Gc)
