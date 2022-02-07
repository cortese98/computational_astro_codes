import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})

t1,lm_petar,hm_petar = np.genfromtxt('segregation_PeTar.txt',usecols=(0,1,2),unpack=True)

t2,lm_total,hm_total=np.genfromtxt('segregation_PeTar_totali.txt',usecols=(0,1,2),unpack=True)


plt.plot(t2,lm_total,color='blue',label='Low mass Total')
plt.plot(t2,hm_total,color='green',label='High Mass Total')
plt.plot(t1,lm_petar,color='red',label='Low Mass Single + Binaries')
plt.plot(t1,hm_petar,color='orange',label='High Mass Single + Binaries')

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Time [Myr]")
plt.ylabel("20% Lagrangian Radius [pc]")
plt.legend(loc='best')


plt.tight_layout()
plt.savefig('mass_segregation_comparison_PeTar.pdf')
plt.show()
