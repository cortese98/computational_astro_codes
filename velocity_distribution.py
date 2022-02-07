import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})



plt.figure(figsize=(8, 6))

vp=[]

vxp_sin,vyp_sin,vzp_sin = np.genfromtxt( "../sim_hydro_m1e41/data.0.single", usecols=(4,5,6),skip_header=1, comments="#", unpack=True)
vp_sin=np.sqrt(vxp_sin**2 + vyp_sin**2 + vzp_sin**2)

vxp_bin,vyp_bin,vzp_bin = np.genfromtxt( "../sim_hydro_m1e41/data.0.binary", usecols=(4,5,6),skip_header=1, comments="#", unpack=True)
vp_bin=np.sqrt(vxp_bin**2 + vyp_bin**2 + vzp_bin**2)

for i in range(len(vp_sin)):
    vp.append(vp_sin[i])
for i in range(len(vp_bin)):
    vp.append(vp_bin[i])

vp=np.array(vp)


a=np.log10(min(vp))
b=np.log10(max(vp))

mybins=np.logspace(a,b,num=50)

plt.hist(vp,bins=mybins,histtype='step',log=True,color='blue',linewidth=2,label="PeTar")


vxn,vyn,vzn = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(4,5,6),skip_header=1, comments="#", unpack=True)

conv = 1.022712165045695 #Conversion factor between Nbody and PeTar velocity unit

vxn *= conv
vyn *= conv
vzn *= conv

vn=np.sqrt(vxn**2 + vyn**2 + vzn**2)

a=np.log10(min(vn))
b=np.log10(max(vn))

mybins=np.logspace(a,b,num=50)

plt.hist(vn,bins=mybins,histtype='step',log=True,color='red',linewidth=2,label="Nbody6++GPU")


plt.xscale("log")
plt.xlabel("|v| [pc/Myr]")
plt.ylabel("Number of stars")
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("velocity_distribution.pdf")
plt.show()

