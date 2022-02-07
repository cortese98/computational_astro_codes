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


rhm_1 = np.zeros(len(files_snap))
rcore_1 = np.zeros(len(files_snap))

rhm_2 = np.zeros(len(files_snap))
rcore_2 = np.zeros(len(files_snap))

for i in files_snap:
    print(sim_path+"data."+str(i)+".single")

    #FIRST DO CALCULATION FOR BINARIES + SINGLE
    
    #SINGLE STARS
    mtot=[]
    xtot=[]
    ytot=[]
    ztot=[]
    vxtot=[]
    vytot=[]
    vztot=[]
    
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".single", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    for j in range (len(m)):
        mtot.append(m[j])
        xtot.append(x[j])
        ytot.append(y[j])
        ztot.append(z[j])
        vxtot.append(vx[j])
        vytot.append(vy[j])
        vztot.append(vz[j])
    
#BINARY STARS
    
    print(sim_path+"data."+str(i)+".binary")
    mb, xb, yb, zb, vxb, vyb, vzb = np.genfromtxt(sim_path+"data."+str(i)+".binary", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    for j in range (0,len(mb)):
        mtot.append(mb[j])
        xtot.append(xb[j])
        ytot.append(yb[j])
        ztot.append(zb[j])
        vxtot.append(vxb[j])
        vytot.append(vyb[j])
        vztot.append(vzb[j])
    
    mtot=np.array(mtot)
    xtot=np.array(xtot)
    ytot=np.array(ytot)
    ztot=np.array(ztot)
    vxtot=np.array(vxtot)
    vytot=np.array(vytot)
    vztot=np.array(vztot)

    dens, xtot, ytot, ztot, vxtot, vytot, vztot = find_and_rescale_cod(mtot, xtot, ytot, ztot, vxtot, vytot, vztot)
    
    rcore_2[i]=lagr_radius(mtot,xtot,ytot,ztot,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm_2[i]=lagr_radius(mtot,xtot,ytot,ztot,lagr=50) #Half-mass radius (50% Lagrangian radius)

    #NOW DO CALCULATION FOR TOTAL STARS

    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i), skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)

    rcore_1[i]=lagr_radius(m,x,y,z,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm_1[i]=lagr_radius(m,x,y,z,lagr=50) #Half-mass radius (50% Lagrangian radius)
     


#Save the radii information in a file for the total stars
X = np.stack((files_snap,rhm_1,rcore_1),axis=-1)
np.savetxt('radii_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')


#Save the radii information in a file for the binary + single
X = np.stack((files_snap,rhm_2,rcore_2),axis=-1)
np.savetxt('radii_PeTar_binary.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')
