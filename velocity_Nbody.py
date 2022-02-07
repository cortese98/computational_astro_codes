import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *

plt.rcParams.update({'font.size': 14})

sim_path = "../m1e4_1_Nbody6_notidal/"

conv = 1.022712165045695 #Conversion factor between Nbody and PeTar velocity unit

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


k=0
for i in range(len(files_snap)):
	
    print(sim_path+"data_Nbody6_"+str(files_snap[i]))
	#Load masses, positions velocities
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    vx *= conv
    vy *= conv
    vz *= conv
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx , vy, vz)
    logm=np.log10(m)
    plt.scatter(vx,vy,s=3,c=logm)
    cbar=plt.colorbar()
    plt.clim(0,2.2)
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    plt.xlabel(r"$V_x$ [pc/Myr]")
    plt.ylabel(r"$V_y$ [pc/Myr]")
    plt.title(f"Time= {files_snap[i]} Myr",loc='center')
    plt.tight_layout()
    plt.savefig(f"velocities_Nbody_noTidal/velocity_Nbody_{k}.png")
    k+=1
    plt.clf()
    
