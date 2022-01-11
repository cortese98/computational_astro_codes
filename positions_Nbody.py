import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *

plt.rcParams.update({'font.size': 14})

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
rhm_old = np.zeros(len(files_snap))
rcore_old = np.zeros(len(files_snap))


for i in range(len(files_snap)):
	
    print(sim_path+"data_Nbody6_"+str(files_snap[i]))
	#Load masses, positions velocities
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    lndens=np.log10(dens)
    plt.scatter(x,y,s=3,c=lndens)
    cbar=plt.colorbar()
    plt.clim(0,5)
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.xlabel("X [pc]")
    plt.ylabel("Y [pc]")
    plt.title(f"Time= {files_snap[i]} Myr",loc='center')
    cbar.set_label(r"$\rho [M_{\odot}/pc^3]$")
    plt.savefig(f"posizioni_Nbody_noTidal/positions_Nbody_{files_snap[i]}_NT.png")
    plt.clf()
    
