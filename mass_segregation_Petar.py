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




low_m_lagr = np.zeros(len(files_snap))
high_m_lagr = np.zeros(len(files_snap))

for i in files_snap:
    print(sim_path+"data."+str(i))
	#Load masses, positions velocities of the single stars
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".single", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
        
            
            
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

        elif(m[j]>=10.):
             m_hm.append(m[j])
             x_hm.append(x[j])
             y_hm.append(y[j])
             z_hm.append(z[j])

             #LOAD DATA FROM THE BINARIES 
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".binary", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
    m1=[]
    x1=[]
    y1=[]
    m2=[]
    x2=[]
    y2=[]
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    for j in range (0,len(m)-1,2):
        m1.append(m[j])
        x1.append(x[j])
        y1.append(y[j])
        m2.append(m[j+1])
        x2.append(x[j+1])
        y2.append(y[j+1])

    m,x,y=binary_center(m1,x1,y1,m2,x2,y2)


    for j in np.arange(len(m)):
        if (m[j]<=10.):
            m_lm.append(m[j])
            x_lm.append(x[j])
            y_lm.append(y[j])
            z_lm.append(z[j])

        elif(m[j]>=10.):
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
    low_m_lagr[i]=lagr_radius(m_lm,x_lm,y_lm,z_lm,lagr=50) #Low mass stars half mass radius
    high_m_lagr[i]=lagr_radius(m_hm,x_hm,y_hm,z_hm,lagr=50) #High mass stars half mass radius

	
#Save the radii information in a file

X = np.stack((files_snap,low_m_lagr,high_m_lagr),axis=-1)
np.savetxt('segregation_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')



#Plot the evolutions of the half mass radii

plt.plot(files_snap,low_m_lagr,color='r',label=r'Low mass stars ($M < 10 M_{\odot}$)')
plt.plot(files_snap,high_m_lagr,color='b',label=r'High mass stars ($M > 10 M_{\odot}$)')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Time [Myr]")
plt.ylabel("Half Mass Radius [pc]")
plt.legend(loc='best')


plt.savefig('plots/mass_segregation_Petar.pdf')
plt.show()

