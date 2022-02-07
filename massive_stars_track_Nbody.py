import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *
plt.rcParams.update({'font.size': 16})


sim_path = "../m1e4_1_Nbody6_notidal/"



files = []

#Find all "data" files in the selected path
for r, d, f in os.walk(sim_path):
    for file in f:
        if 'data' in file: 
            files.append({"name":os.path.join(file[:4]), "nsnap":os.path.join(file[12:])})


files_snap = []
for f in files:
    try:
        isinstance(float(f["nsnap"]), float)
        files_snap.append(float(f["nsnap"]))
    except:
        print("",end="")
files_snap = np.sort(np.array(files_snap))


r_massive = []
t_massive= []
m_massive= []


for i in range(len(files_snap)):

    print(sim_path+"data_Nbody6_"+str(files_snap[i]))
	#Load masses, positions velocities
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    
    #evaluate density and rescale to the center of density
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    for j in range (len(m)):
        if (m[j] > 10.):
            r= np.sqrt(x[j]**2 + y[j]**2 + z[j]**2)
            r_massive.append(r)
            t_massive.append(files_snap[i])
            m_massive.append(m[j])

r_massive=np.array(r_massive)
t_massive=np.array(t_massive)
m_massive=np.array(m_massive)
m_massive=np.log10(m_massive)

plt.scatter(t_massive,r_massive, s=6 ,c=m_massive ,label="Massive stars")
cbar=plt.colorbar()
plt.clim(1,2.1)
plt.xlabel("Time [Myr]")
plt.ylabel("r [pc]")
cbar.set_label("log(M) [$M_{\odot}$]")
plt.xscale("log")
plt.ylim(-300,12000)
#plt.yscale("log")
plt.title("Nbody6")
plt.legend()
plt.savefig("Nbody_Massive_stars_track.pdf",bbox_inches='tight')
plt.show()
