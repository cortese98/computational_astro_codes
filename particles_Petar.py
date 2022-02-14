import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})


t_p,n_p,n_p_bin=np.genfromtxt("total_mass_PeTar.txt",usecols=(0,3,4),unpack=True)


plt.xlabel("t [Myr]")
plt.ylabel("N")
plt.plot(t_p,n_p,color='blue',linewidth=3,label='PeTar total')
plt.plot(t_p,n_p_bin,color='green',linewidth=3,label='Petar single+binaries')
plt.legend()
plt.tight_layout()
#plt.savefig("Total_mass_compare.pdf")
plt.show()
