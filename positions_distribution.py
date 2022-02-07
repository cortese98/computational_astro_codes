import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})



plt.figure(figsize=(8, 6))

rp=[]

xp_sin,yp_sin,zp_sin = np.genfromtxt( "../sim_hydro_m1e41/data.0", usecols=(1,2,3),skip_header=1, comments="#", unpack=True)
rp_sin=np.sqrt(xp_sin**2 + yp_sin**2 + zp_sin**2)



a=np.log10(min(rp_sin))
b=np.log10(max(rp_sin))

mybins=np.logspace(a,b,num=50)

plt.hist(rp_sin,bins=mybins,histtype='step',log=True,color='blue',linewidth=2,label="PeTar",alpha=0.6)


xn,yn,zn = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(1,2,3),skip_header=1, comments="#", unpack=True)


rn=np.sqrt(xn**2 + yn**2 + zn**2)

a=np.log10(min(rn))
b=np.log10(max(rn))

mybins=np.logspace(a,b,num=50)

plt.hist(rn,bins=mybins,histtype='step',log=True,color='red',linewidth=2,label="Nbody6++GPU",alpha=0.6)


plt.xscale("log")
plt.xlabel("|r| [pc]")
plt.ylabel("Number of stars")
plt.legend(loc='upper left')
plt.tight_layout()
#plt.savefig("velocity_distribution.pdf")
plt.show()

