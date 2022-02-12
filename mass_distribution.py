import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})




fig,ax = plt.subplots(2,1,figsize=(8,8),sharex=True)
#plt.subplots_adjust(wspace=0.00)
plt.subplots_adjust(hspace=0.00)

#READ THE INITIAL MASS OF THE STARS

# PETAR TOTAL STARS

m0p = np.genfromtxt( "../sim_hydro_m1e41/data.0", usecols=(0),skip_header=1, comments="#", unpack=True)
a=np.log10(min(m0p))
b=np.log10(max(m0p))
mybins=np.logspace(a,b,num=50)
ax[0].hist(m0p,bins=mybins,histtype='step',log=True,linewidth=2,color='orange', label="Petar, total stars")
ax[1].hist(m0p,bins=mybins,histtype='step',log=True,linewidth=2,color='orange', label="Petar, total stars")


#PETAR SINGLE+BINARY STARS



m0tot=[]

m0sing = np.genfromtxt( "../sim_hydro_m1e41/data.0.single", usecols=(0),skip_header=1, comments="#", unpack=True)
m0bin = np.genfromtxt( "../sim_hydro_m1e41/data.0.binary", usecols=(0),skip_header=1, comments="#", unpack=True)

for i in range (len(m0sing)):
    m0tot.append(m0sing[i])
for i in range (len(m0bin)):
    m0tot.append(m0bin[i])
m0tot=np.array(m0tot)
a=np.log10(min(m0tot))
b=np.log10(max(m0tot))
mybins=np.logspace(a,b,num=50)
ax[1].hist(m0tot,bins=mybins,histtype='step',log=True,linewidth=2,color='green', label="Petar, single + binaries")

ax[0].set_xscale("log")
ax[1].set_xscale("log")





#  NBODY

m0N = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(0),skip_header=1, comments="#", unpack=True)
a=np.log10(min(m0N))
b=np.log10(max(m0N))
mybins=np.logspace(a,b,num=50)
ax[0].hist(m0N,bins=mybins,histtype='step',log=True, linewidth=2,color='blue', label="Nbody")




#PLOT THE MASS DISTRIBUTIONS 



#plt.xscale=("log")
#ax[0].set_xlabel("M [$M_{\odot}$]")
ax[0].set_ylabel("Number of stars")
ax[1].set_xlabel("M [$M_{\odot}$]")
ax[1].set_ylabel("Number of stars")
ax[0].legend()
ax[1].legend()
#fig.tight_layout()
#plt.savefig("Mass_distribution.pdf")
plt.show()

