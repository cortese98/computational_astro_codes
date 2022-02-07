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

m_tot_bin=np.zeros(len(files_snap))

n_tot=np.zeros(len(files_snap))
n_totbin=np.zeros(len(files_snap))

for i in files_snap:
    print(sim_path+"data."+str(i))
    #Load masses, positions velocities
    m = np.genfromtxt(sim_path+"data."+str(i), skip_header=1, comments="#", unpack=True, usecols=(0))
    msing = np.genfromtxt(sim_path+"data."+str(i)+".single", skip_header=1, comments="#", unpack=True, usecols=(0))
    mbin= np.genfromtxt(sim_path+"data."+str(i)+".binary", skip_header=1, comments="#", unpack=True, usecols=(0))
    m_tot[i]= np.sum(m)
    m_tot_bin[i] = np.sum(msing) + np.sum(mbin)
    n_tot[i]=len(m)
    n_totbin[i]=len(msing) + len(mbin)
	
#Save the radii information in a file
X = np.stack((files_snap,m_tot,m_tot_bin,n_tot,n_totbin),axis=-1)
np.savetxt('total_mass_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f %.1f %.1f')
