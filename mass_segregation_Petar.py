import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *

plt.rcParams.update({'font.size': 18})

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

    mtot=[]
    xtot=[]
    ytot=[]
    ztot=[]
    vxtot=[]
    vytot=[]
    vztot=[]

    print(sim_path+"data."+str(i))

    #SINGLE STARS
    
    m, x, y, z, vx, vy, vz = np.genfromtxt(sim_path+"data."+str(i)+".single", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
#    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)
    for j in range (len(m)):
        mtot.append(m[j])
        xtot.append(x[j])
        ytot.append(y[j])
        ztot.append(z[j])
        vxtot.append(vx[j])
        vytot.append(vy[j])
        vztot.append(vz[j])


    #BINARY STARS
    

    mb, xb, yb, zb, vxb, vyb, vzb = np.genfromtxt(sim_path+"data."+str(i)+".binary", skip_header=1, comments="#", unpack=True, usecols=(0,1,2,3,4,5,6))
#    dens, xb, yb, zb, vxb, vyb, vzb = find_and_rescale_cod(mb, xb, yb, zb, vxb, vyb, vzb)
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


    #ANALYSE THE MASS SEGREGATION
    
    m_lm  = []
    x_lm  = []
    y_lm  = []
    z_lm  = []
    m_hm  = []
    x_hm  = []
    y_hm  = []
    z_hm  = []

    for j in range (len(mtot)):
        if (mtot[j] < 10.):
            m_lm.append(mtot[j])
            x_lm.append(xtot[j])
            y_lm.append(ytot[j])
            z_lm.append(ztot[j])
        elif(mtot[j] >= 10.):
            m_hm.append(mtot[j])
            x_hm.append(xtot[j])
            y_hm.append(ytot[j])
            z_hm.append(ztot[j])
            
    m_lm=np.array(m_lm)
    x_lm=np.array(x_lm)
    y_lm=np.array(y_lm)
    z_lm=np.array(z_lm)
    m_hm=np.array(m_hm)
    x_hm=np.array(x_hm)
    y_hm=np.array(y_hm)
    z_hm=np.array(z_hm)
    

    low_m_lagr[i]=lagr_radius(m_lm,x_lm,y_lm,z_lm,lagr=20) #Low mass stars 20% lagrangian radius
    high_m_lagr[i]=lagr_radius(m_hm,x_hm,y_hm,z_hm,lagr=20) #High mass stars 20% lagrangian radius
    print(len(mtot),np.sum(mtot))
    print(len(m_lm),np.sum(m_lm))
    print (len(m_hm),np.sum(m_hm))
	
#Save the radii information in a file

X = np.stack((files_snap,low_m_lagr,high_m_lagr),axis=-1)
np.savetxt('segregation_PeTar.txt',X,delimiter="        ",fmt='%.1f %.8f %.8f')



#Plot the evolutions of the lagrangian radii

plt.plot(files_snap,low_m_lagr,color='r',label=r'Low mass stars ($M < 10 M_{\odot}$)')
plt.plot(files_snap,high_m_lagr,color='b',label=r'High mass stars ($M > 10 M_{\odot}$)')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Time [Myr]")
plt.ylabel("20% Lagrangian Radius [pc]")
plt.legend(loc='best')


plt.savefig('plots/mass_segregation_Petar2.pdf')
plt.show()

