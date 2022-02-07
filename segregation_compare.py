import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

t1,lm_petar,hm_petar = np.genfromtxt('segregation_PeTar_totali.txt',usecols=(0,1,2),unpack=True)

t2,lm_nbody,hm_nbody=np.genfromtxt('segregation_Nbody.txt',usecols=(0,1,2),unpack=True)


plt.plot(t1,lm_petar,color='red',label='Low Mass PeTar')
plt.plot(t1,hm_petar,color='orange',label='High Mass PeTar')
plt.plot(t2,lm_nbody,color='blue',label='Low Mass Nbody6++')
plt.plot(t2,hm_nbody,color='green',label='High Mass Nbody6++')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Time [Myr]")
plt.ylabel("20% Lagrangian Radius [pc]")
plt.legend(loc='best')


plt.savefig('mass_segregation_comparison_noTidal.pdf')
plt.show()
