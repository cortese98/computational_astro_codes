import numpy as np
import petar
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 20})


filer='data.lagr'
ral=petar.Lagrangian()
ral.loadtxt(filer)
core=petar.Core()
filec='data.core'
core.loadtxt(filec)

t, rh, rc = np.genfromtxt('radii.txt', dtype=float, skip_header=1,unpack=True)


fig, ax = plt.subplots(2,1,sharex='col', figsize=(8,8))
plt.subplots_adjust(wspace=0.00)
plt.subplots_adjust(hspace=0.00)
ax[0].plot(ral.r[:,0],ral.r[:,3], c='teal',label='Petar tool')


ax[1].plot(core.time,core.rc, c='crimson',label='Petar tool')

ax[1].set_xlabel('t (Myr)')
ax[0].set_ylabel(r'$r_{\rm{h}}$ (pc)')
ax[1].set_ylabel(r'$r_{\rm{c}}$ (pc)')
ax[0].set_xscale("log")
ax[0].set_yscale("log")
ax[1].set_xscale("log")
ax[1].set_yscale("log")
ax[0].legend(loc='best')
ax[1].legend(loc='best')
plt.tight_layout()

plt.savefig('rh_rc.pdf')
plt.show()
