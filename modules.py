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

def binary_center(m1,x1,y1,m2,x2,y2):
    m=np.zeros(len(m1))
    x=np.zeros(len(m1))
    y=np.zeros(len(m1))
    for j in range(len(m)):
      m[j]=m1[j]+m2[j]  
      x[j]= (m1[j]*x1[j]+m2[j]*x2[j])/(m[j])
      y[j]= (m1[j]*y1[j] + m2[j]*y2[j])/m[j]
    return m,x,y
