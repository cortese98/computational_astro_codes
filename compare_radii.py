import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

#Read the core and the half mass radii from the files created by analysis script


t1,rhm1,rcore1=np.genfromtxt('radii_PeTar.txt',usecols=(0,1,2),unpack=True)
t1b,rhm1b,rcore1b=np.genfromtxt('radii_PeTar_binary.txt',usecols=(0,1,2),unpack=True)
t2,rhm2,rcore2=np.genfromtxt('radii_Nbody_noTidal.txt',usecols=(0,1,2),unpack=True)
                    

#Plot the evolution of the radii


fig, ax = plt.subplots(2,1,sharex='col', figsize=(8,8))
plt.subplots_adjust(wspace=0.00)
plt.subplots_adjust(hspace=0.00)
ax[0].plot(t1,rhm1, c='orange',label='PeTar Total')
ax[0].plot(t2,rhm2, c='blue',label='Nbody6')
ax[0].plot(t1b,rhm1b, c='red',label='PeTar Single + Binaries')

ax[1].plot(t2,rcore2, c='blue',label='Nbody6')
ax[1].plot(t1,rcore1, c='orange',label='PeTar Total')
ax[1].plot(t1b,rcore1b, c='red',label='PeTar Single + Binaries')


ax[1].set_xlabel('t (Myr)')
ax[0].set_ylabel(r'$r_{\rm{h}}$ (pc)')
ax[1].set_ylabel(r'$r_{\rm{c}}$ (pc)')
ax[0].set_yscale("log")
ax[0].set_xscale("log")
ax[1].set_yscale("log")
ax[1].set_xscale("log")
ax[0].legend(loc='best')
ax[1].legend(loc='best')
plt.tight_layout()
plt.savefig('rh_rc_Compare.pdf')
plt.show()
