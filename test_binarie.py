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




rhm = np.zeros(len(files_snap))
rcore = np.zeros(len(files_snap))

for i in range(0,len(files_snap),2):
    
    print(sim_path+"data."+str(i))
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    m1=[]
    x1=[]
    y1=[]
    m2=[]
    x2=[]
    y2=[]
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    for j in range (0,len(m),2):
        m1.append(m[j])
        x1.append(x[j])
        y1.append(y[j])
        m2.append(m[j+1])
        x2.append(x[j+1])
        y2.append(y[j+1])

    m,x,y=binary_center(m1,x1,y1,m2,x2,y2)
    plt.scatter(x1,y1,s=4,c='red',alpha=0.5)
    plt.scatter(x2,y2,s=4,c='blue',alpha=0.5)
    plt.scatter(x,y,s=4,c='green')
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.xlabel("X [pc]")
    plt.ylabel("Y [pc]")
    plt.title(f"Time= {i} Myr",loc='center')
    #plt.savefig(f'binarie_petar/binarie_PeTar_{i}.png')
    plt.show()
    plt.clf()
