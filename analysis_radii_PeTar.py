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

dx = 0.0425247
dy = -0.0215198
dz = -0.073970

rhm = np.zeros(len(files_snap))
rcore = np.zeros(len(files_snap))

for i in files_snap:
    print(sim_path+"data."+str(i))

    #SINGLE STARS
    mtot=[]
    xtot=[]
    ytot=[]
    ztot=[]
    
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".single", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    for j in range (len(m)):
        mtot.append(m[j])
        xtot.append(x[j])
        ytot.append(y[j])
        ztot.append(z[j])
    #BINARY STARS

    mb, xb, yb, zb, vxb, vyb, vzb = np.genfromtxt(sim_path+"data."+str(i)+".binary", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    dens, xb, yb, zb, vxb, vyb, vzb = find_and_rescale_cod(mb, xb, yb, zb, vxb, vyb, vzb)
    m1=[]
    x1=[]
    y1=[]
    z1=[]
    m2=[]
    x2=[]
    y2=[]
    z2=[]
    for j in range (0,len(mb)-1,2):
        m1.append(mb[j])
        x1.append(xb[j])
        y1.append(yb[j])
        z1.append(zb[j])
        m2.append(mb[j+1])
        x2.append(xb[j+1])
        y2.append(yb[j+1])
        z2.append(zb[j+1])
    mb,xb,yb,zb = binary_center(m1,x1,y1,z1,m2,x2,y2,z2)
    for j in range (0,len(mb)):
        mtot.append(mb[j])
        xtot.append(xb[j])
        ytot.append(yb[j])
        ztot.append(zb[j])
    
    mtot=np.array(mtot)
    xtot=np.array(xtot)
    ytot=np.array(ytot)
    ztot=np.array(ztot)
    

    
    rcore[i]=lagr_radius(mtot,xtot,ytot,ztot,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm[i]=lagr_radius(mtot,xtot,ytot,ztot,lagr=50) #Half-mass radius (50% Lagrangian radius)
	
	
#Save the radii information in a file
X = np.stack((files_snap,rhm,rcore),axis=-1)
np.savetxt('radii_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')
