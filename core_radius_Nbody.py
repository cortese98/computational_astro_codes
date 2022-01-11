import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat

sim_path = "../m1e4_1_Nbody6/"

#Function to evaluate density around each star. Density is calculated by considering the sphere
#that contains the closest k neighbours

def density(m,x,y,z,vx,vy,vz,k=500):
    pos = np.stack((x, y, z),axis=-1)
    pos_tree=spat.cKDTree(pos)
    denr=0.

    rho = np.zeros(len(m))

    for j in np.arange(len(m)):
        indneigh=pos_tree.query(pos[j],k)[1]
        dist_tree = np.sqrt((x[indneigh]-x[j])**2.+(y[indneigh]-y[j])**2.+(z[indneigh]-z[j])**2.)

        den=len(m[indneigh])/(4./3.*np.pi*(max(dist_tree))**3.)
        rho[j] = den

        if(den>denr):
            m_big=m[indneigh]
            x_big=x[indneigh]
            y_big=y[indneigh]
            z_big=z[indneigh]
            vx_big=vx[indneigh]
            vy_big=vy[indneigh]
            vz_big=vz[indneigh]
            denr=den

    x_cod=np.sum(x_big*m_big)/(np.sum(m_big))
    y_cod=np.sum(y_big*m_big)/(np.sum(m_big))
    z_cod=np.sum(z_big*m_big)/(np.sum(m_big))
    vx_cod=np.sum(vx_big*m_big)/(np.sum(m_big))
    vy_cod=np.sum(vy_big*m_big)/(np.sum(m_big))
    vz_cod=np.sum(vz_big*m_big)/(np.sum(m_big))
     

    return rho,x_cod, y_cod, z_cod, vx_cod, vy_cod, vz_cod

#Function to rescale positions and velocities to the center of density
def find_and_rescale_cod(m,x,y,z,vx,vy,vz,k=500):

    rho, x_cod, y_cod, z_cod, vx_cod, vy_cod, vz_cod = density(m,x,y,z,vx,vy,vz,k)

    #Rescale the positions and velocities in their c.o.d.
    x = x - x_cod
    y = y - y_cod
    z = z - z_cod
    vx = vx - vx_cod
    vy = vy - vy_cod
    vz = vz - vz_cod
    
    return rho,x,y,z,vx,vy,vz

#Function to evaluate the n% lagrangian radius
def lagr_radius(m,x,y,z, lagr=50):
    r_vect = np.sqrt(x**2+y**2+z**2)
    Mtot = np.sum(m)

    rbin = np.linspace(min(r_vect),max(r_vect),4000)
    mbin_r = np.zeros(len(rbin))

    for j in range(len(rbin)):     
        mappovect= np.where(r_vect<rbin[j],m,0)
        mbin_r[j] = np.sum(mappovect)

    r_lagr = np.interp(Mtot/(100./lagr), mbin_r, rbin)

    return r_lagr



################################################################
#main
################################################################


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
    rcore_old[i]=lagr_radius(m,x,y,z,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm_old[i]=lagr_radius(m,x,y,z,lagr=50) #Half-mass radius (50% Lagrangian radius)
    
    #evaluate density and rescale to the center of density
    dens, x, y, z, vx, vy, vz = find_and_rescale_cod(m, x, y, z, vx, vy, vz)

    rcore[i]=lagr_radius(m,x,y,z,lagr=10) #Core radius, defined as 10% lagrangian radius
    rhm[i]=lagr_radius(m,x,y,z,lagr=50) #Half-mass radius (50% Lagrangian radius)
	


fig, ax = plt.subplots(2,1,sharex='col', figsize=(6,6))
plt.subplots_adjust(wspace=0.00)
plt.subplots_adjust(hspace=0.00)
ax[0].plot(files_snap,rhm_old, c='teal',label='Nbody6')
ax[0].plot(files_snap,rhm, c='blue',label='Rescaled with density')

ax[1].plot(files_snap,rcore_old, c='crimson',label='Nbody6')
ax[1].plot(files_snap,rcore, c='orange',label='Rescalde with density')
ax[1].set_xlabel('t (Myr)',fontsize=12)
ax[0].set_ylabel(r'$r_{\rm{h}}$ (pc)', fontsize=12)
ax[1].set_ylabel(r'$r_{\rm{c}}$ (pc)',fontsize=12)
plt.yscale("log")
plt.xscale("log")
ax[0].legend(loc='best')
ax[1].legend(loc='best')

plt.savefig('rh_rc_Nbody.pdf')
plt.show()

