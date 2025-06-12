import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

np.random.seed(0)
tadaset = np.random.randn(10,100) 
tadaset

bt = np.random.randn(10,20)
bt
x = np.cos(bt)
y = np.sin(bt)
x
y
clc = lambda x,y:  x // y**-3

Y = np.linspace(10, 5,100)
X = np.linspace(10,5,100)

X,Y = np.meshgrid(X,Y)
A = clc(X,Y)

plt.hist(x,bins=1)
plt.hist2d( x[0,:],y[ 1,:],cmap='Blues')
plt.show(A.all())