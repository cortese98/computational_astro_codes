import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat

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

m_tot=np.zeros(len(files_snap))
n_tot=np.zeros(len(files_snap))

for i in range(len(files_snap)):
	
    print(sim_path+"data_Nbody6_"+str(files_snap[i]))
	#Load masses, positions velocities
    m = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0))
    m_tot[i]=np.sum(m)
    n_tot[i]=len(m)
	
#Save the radii information in a file	
X = np.stack((files_snap,m_tot,n_tot),axis=-1)
np.savetxt('total_mass_Nbody.txt',X,delimiter="        ",fmt='%.4f %.8f %.1f')
