import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import scipy.spatial as spat
from modules import *


mp,xp,yp,zp,vxp,vyp,vzp = np.genfromtxt( "../sim_hydro_m1e41/data.0.single", usecols=(0,1,2,3,4,5,6),skip_header=1, comments="#", unpack=True)

mb,xb,yb,zb,vxb,vyb,vzb = np.genfromtxt( "../sim_hydro_m1e41/data.0.binary", usecols=(0,1,2,3,4,5,6),skip_header=1, comments="#", unpack=True)

mt,xt,yt,zt,vxt,vyt,vzt = np.genfromtxt( "../sim_hydro_m1e41/data.0", usecols=(0,1,2,3,4,5,6),skip_header=1, comments="#", unpack=True)

mn,xn,yn,zn,vxn,vyn,vzn = np.genfromtxt( "../m1e4_1_Nbody6_notidal/data_Nbody6_0.0", usecols=(0,1,2,3,4,5,6),comments="#", skip_header=1,unpack=True)
conv = 1.022712165045695
for i in range (100,150):
    print ("NUOVA PARTICELLA")
    for j in range (0,len(mn)):
        m=np.abs((mp[i]-mn[j]))
        if (m<0.000001):
            print ("compatible")
            x= xp[i]-xn[j]
            y= yp[i]-yn[j]
            z= zp[i]-zn[j]
            vx= np.abs(vxp[i]-vxn[j]*conv)
            vy = np.abs(vyp[i]-vyn[j]*conv)
            vz= np.abs(vzp[i]-vzn[j]*conv)
            r= np.sqrt(x*x + y*y + z*z)
            v= np.sqrt(vx*vx + vy*vy + vz*vz)
            print (x,y,z)
            print (vx,vy,vz)
print(len(mt))
print(len(xp))
print(len(xb))
print(len(xn))





