import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *

plt.rcParams.update({'font.size': 14})

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




for i in files_snap:
    
    print(sim_path+"data."+str(i))
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i), skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    plt.scatter(vx,vy,s=3)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.xlabel(r"$V_x$ [km/s]")
    plt.ylabel(r"$V_y$ [km/s]")
    plt.title(f"Time= {i} Myr",loc='center')
    plt.savefig(f'velocities_Petar/velocity_PeTar_{i}.png')
    plt.clf()

	
    
