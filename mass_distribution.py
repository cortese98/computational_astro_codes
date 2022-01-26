import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})

# PETAR

m0p = np.genfromtxt( "../sim_hydro_m1e41/data.0", usecols=(0),skip_header=1, comments="#", unpack=True)
a=np.log10(min(m0p))
b=np.log10(max(m0p))
mybins=np.logspace(a,b,num=20)
plt.hist(m0p,bins=mybins,histtype='step',log=True,linewidth=2, label="Petar, t=0 Myr")
m0_tot=np.sum(m0p)



mfp = np.genfromtxt( "../sim_hydro_m1e41/data.117", usecols=(0),skip_header=1, comments="#", unpack=True)
l=np.log10(min(mfp))
m=np.log10(max(mfp))
mybins=np.logspace(l,m,num=20)
plt.hist(mfp,bins=mybins,histtype='step',log=True,linewidth=2, label="Petar, t=117 Myr")
mf_tot=np.sum(mfp)
print("Initial mass Petar: ", m0_tot)
print("Final mass Petar: ", mf_tot)

#  NBODY

m0N = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(0),skip_header=1, comments="#", unpack=True)
a=np.log10(min(m0N))
b=np.log10(max(m0N))
mybins=np.logspace(a,b,num=20)
plt.hist(m0N,bins=mybins,histtype='step',log=True, linewidth=2, label="Nbody, t=0 Myr")
m0_tot=np.sum(m0N)



mfN = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_117.133", usecols=(0),skip_header=1, comments="#", unpack=True)
l=np.log10(min(mfN))
m=np.log10(max(mfN))
mybins=np.logspace(l,m,num=20)
plt.hist(mfN,bins=mybins,histtype='step',log=True, linewidth=2, label="Nbody, t=117.133 Myr")
mf_tot=np.sum(mfN)

print("Initial mass Nbody: ", m0_tot)
print("Final mass Nbody: ", mf_tot)





plt.xscale=("log")
plt.xlabel("M [$M_{\odot}$]")
plt.ylabel("Number of stars")
plt.tight_layout()
plt.legend()
plt.show()

