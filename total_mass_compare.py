import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})


t_nb,m_nb=np.genfromtxt("total_mass_Nbody.txt",usecols=(0,1),unpack=True)

t_p,m_p,m_p_bin=np.genfromtxt("total_mass_PeTar.txt",usecols=(0,1,2),unpack=True)


plt.xlabel("t [Myr]")
plt.ylabel(r"$M [M_{\odot}]$")
plt.plot(t_nb,m_nb,color='red',label='Nbody')
plt.plot(t_p,m_p,color='blue',label='PeTar total')
plt.plot(t_p,m_p_bin,color='green',label='Petar single+binaries')
plt.legend()
plt.tight_layout()
plt.savefig("Total_mass_compare.pdf")
plt.show()
