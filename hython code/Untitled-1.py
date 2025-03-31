"""
Created on Wed Feb  5 10:32:46 2025

@author: rama k
"""
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.dataset import load_iris
from mpl_toolkits.mplot3d import Axes3D

ax = plt.axes(projection = '3d')

bt = np.random.randn(10,20)
bt
x = np.cos(bt)
y = np.sin(bt)

clc = lambda: x // y**-3

ax.scatter(x,y,c=y) 
clc()