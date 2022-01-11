import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *


mp,xp,yp,zp,vxp,vyp,vzp = np.genfromtxt( "../sim_hydro_m1e41/data.0.single", usecols=(0,1,2,3,4,5,6),skip_header=1, comments="#", unpack=True)

mn,xn,yn,zn,vxn,vyn,vzn = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(0,1,2,3,4,5,6),comments="#", skip_header=1,unpack=True)
deltax=[]
deltavx=[]
for i in range (100,120):
    print ("NUOVA PARTICELLA")
    for j in range (0,len(mn)):
        m=np.abs((mp[i]-mn[j]))

        if (m<0.000001):
            print ("compatible")
            x= np.abs(xp[i]-xn[j])
            y= np.abs(yp[i]-yn[j])
            z= np.abs(zp[i]-zn[j])
            vx= np.abs(vxp[i]-vxn[j])
            vy = np.abs(vxp[i]-vyn[j])
            vz= np.abs(vzp[i]-vzn[j])
            r= np.sqrt(x*x + y*y + z*z)
            v= np.sqrt(vx*vx + vy*vy + vz*vz)
            print (r,v)
        

#for i in range (0,len():
#   m=np.abs(mp[i]-mn[i])
#    x=np.abs(xp[i]-xn[i])
#    y=np.abs(yp[i]-yn[i])
#    z=np.abs(zp[i]-zn[i])
#    vx=np.abs(vxp[i]-vxn[i])
#    vy=np.abs(vyp[i]-vyn[i])
#    vz=np.abs(vzp[i]-vzn[i])
#    print (m,x,y,z,vx,vy,vz)


