import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat



sim_path = "../sim_hydro_m1e41/"
	
files = []

#Find all "data" files in the selected path
for r, d, f in os.walk(sim_path):
    for file in f:
        if 'data' in file: 
            files.append({"name":os.path.join(file[:4]), "nsnap":os.path.join(file[5:])})
            #print(files[-1])
			
#Discard files that are not data.0, data.1,....		
files_snap = []
for f in files:
    try:
        isinstance(int(f["nsnap"]), int)
        files_snap.append(int(f["nsnap"]))
    except:
        print("",end="")
files_snap = np.sort(np.array(files_snap))




m_tot = np.zeros(len(files_snap))


for i in files_snap:
    print(sim_path+"data."+str(i))
    #Load masses, positions velocities
    m = np.genfromtxt(sim_path+"data."+str(i), skip_header=1, comments="#", unpack=True, usecols=(0))
    m_tot[i]=np.sum(m)
	
#Save the radii information in a file
X = np.stack((files_snap,m_tot),axis=-1)
np.savetxt('total_mass_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f')
