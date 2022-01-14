import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})


t1,rhm1,rcore1=np.genfromtxt('radii_PeTar.txt',usecols=(0,1,2),unpack=True)
t2,rhm2,rcore2=np.genfromtxt('radii_Nbody_noTidal.txt',usecols=(0,1,2),unpack=True)

                    

fig, ax = plt.subplots(2,1,sharex='col', figsize=(6,6))
plt.subplots_adjust(wspace=0.00)
plt.subplots_adjust(hspace=0.00)
ax[0].plot(t1,rhm1, c='teal',label='PeTar')
ax[0].plot(t2,rhm2, c='blue',label='Nbody6')

ax[1].plot(t2,rcore2, c='crimson',label='Nbody6')
ax[1].plot(t1,rcore1, c='orange',label='PeTar')
ax[1].set_xlabel('t (Myr)',fontsize=12)
ax[0].set_ylabel(r'$r_{\rm{h}}$ (pc)', fontsize=12)
ax[1].set_ylabel(r'$r_{\rm{c}}$ (pc)',fontsize=12)
ax[0].set_yscale("log")
ax[0].set_xscale("log")
ax[1].set_yscale("log")
ax[1].set_xscale("log")
ax[0].legend(loc='best')
ax[1].legend(loc='best')

plt.savefig('rh_rc_Compare.png')
plt.show()
