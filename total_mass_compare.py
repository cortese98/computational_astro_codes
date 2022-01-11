import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})


t_nb,m_nb=np.genfromtxt("total_mass_Nbody.txt",unpack=True)

t_p,m_p=np.genfromtxt("total_mass_PeTar.txt",unpack=True)


plt.xlabel("t [Myr]")
plt.ylabel(r"$M [M_{\odot}]$")
plt.plot(t_nb,m_nb,color='red',label='Nbody')
plt.plot(t_p,m_p,color='blue',label='PeTar')
plt.legend()
plt.show()
