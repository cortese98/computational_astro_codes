import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *




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


rhm = np.zeros(len(files_snap))
rcore = np.zeros(len(files_snap))


for i in range(len(files_snap)):
	
    print(sim_path+"data_Nbody6_"+str(files_snap[i]))
	#Load masses, positions velocities
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    
    #evaluate density and rescale to the center of density
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)

    rcore[i]=lagr_radius(m,x,y,z,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm[i]=lagr_radius(m,x,y,z,lagr=50) #Half-mass radius (50% Lagrangian radius)
	
	
#Save the radii information in a file	
X = np.stack((files_snap,rhm,rcore),axis=-1)
np.savetxt('radii_Nbody_noTidal.txt',X,delimiter="        ",fmt='%.4f %.8f %.8f')
