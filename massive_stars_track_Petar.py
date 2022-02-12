import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *
plt.rcParams.update({'font.size': 16})



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



r_massive = []
t_massive= []
m_massive= []


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

    #Rescales for the density center

    dens, xtot, ytot, ztot, vxtot, vytot, vztot = find_and_rescale_cod(mtot, xtot, ytot, ztot, vxtot, vytot, vztot)

    #Take the massive stars and evaluate the distance from the center
    
    for j in range (len(mtot)):
        if (mtot[j] > 10.):
            r= np.sqrt(xtot[j]**2 + ytot[j]**2 + ztot[j]**2)
            r_massive.append(r)
            t_massive.append(i)
            m_massive.append(mtot[j])

r_massive=np.array(r_massive)
t_massive=np.array(t_massive)
m_massive=np.array(m_massive)
m_massive=np.log10(m_massive)


#Plot the massive stars tracks

plt.scatter(t_massive,r_massive, s=6, c=m_massive , label="Massive stars")
cbar=plt.colorbar()
plt.xlabel("Time [Myr]")
plt.ylabel("|r| [pc]")
plt.title("PeTar")
plt.clim(1,2.1)
plt.ylim(-300,12000)
cbar.set_label("log(M) [$M_{\odot}$]")
plt.xscale("log")
plt.legend()
#plt.yscale("log")
plt.savefig("PeTar_Massive_stars_track.pdf",bbox_inches='tight')

#plt.show()

    
