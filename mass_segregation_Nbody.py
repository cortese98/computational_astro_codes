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


low_m_lagr = np.zeros(len(files_snap))
high_m_lagr = np.zeros(len(files_snap))


for i in range(len(files_snap)):
	
    print(sim_path+"data_Nbody6_"+str(files_snap[i]))

    #Load masses, positions velocities
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data_Nbody6_"+str(files_snap[i]), comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    
    #evaluate density and rescale to the center of density
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)

    m_lm  = []
    x_lm  = []
    y_lm  = []
    z_lm  = []
    m_hm  = []
    x_hm  = []
    y_hm  = []
    z_hm  = []

    for j in np.arange(len(m)):
        if (m[j]<=10.):
            m_lm.append(m[j])
            x_lm.append(x[j])
            y_lm.append(y[j])
            z_lm.append(z[j])

        elif(m[j]>10.):
             m_hm.append(m[j])
             x_hm.append(x[j])
             y_hm.append(y[j])
             z_hm.append(z[j])
    m_lm  = np.array(m_lm)
    x_lm  = np.array(x_lm)
    y_lm  = np.array(y_lm)
    z_lm  = np.array(z_lm)
    m_hm  = np.array(m_hm)
    x_hm  = np.array(x_hm)
    y_hm  = np.array(y_hm)
    z_hm  = np.array(z_hm)
    low_m_lagr[i]=lagr_radius(m_lm,x_lm,y_lm,z_lm,lagr=20) #Low mass stars 20% lagrangian radius
    high_m_lagr[i]=lagr_radius(m_hm,x_hm,y_hm,z_hm,lagr=20) #High mass stars 20& lagrangian radius
    print(len(m_lm),np.sum(m_lm))
    print (len(m_hm),np.sum(m_hm))
    print(len(m),np.sum(m))
    
	
#Save the radii information in a file

X = np.stack((files_snap,low_m_lagr,high_m_lagr),axis=-1)
np.savetxt('segregation_Nbody.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')



#Plot the evolutions of the two radii

plt.plot(files_snap,low_m_lagr,color='r',label=r'Low mass stars ($M < 10 M_{\odot}$)')
plt.plot(files_snap,high_m_lagr,color='b',label=r'High mass stars ($M > 10 M_{\odot}$)')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Time [Myr]")
plt.ylabel("20% Lagrangian Radius [pc]")
plt.legend(loc='best')


plt.savefig('mass_segregation_Nbody_noTidal.pdf')
plt.show()

