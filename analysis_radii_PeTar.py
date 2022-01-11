import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *
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




rhm = np.zeros(len(files_snap))
rcore = np.zeros(len(files_snap))

for i in files_snap:
	print(sim_path+"data."+str(i))
	#Load masses, positions velocities
	m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i), skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))

	#evaluate density and rescale to the center of density
	dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)

	rcore[i]=lagr_radius(m,x,y,z,lagr=10) #Core radius, defined as 10% lagrangian radius
	rhm[i]=lagr_radius(m,x,y,z,lagr=50) #Half-mass radius (50% Lagrangian radius)
	
	
#Save the radii information in a file
X = np.stack((files_snap,rhm,rcore),axis=-1)
np.savetxt('radii_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')
