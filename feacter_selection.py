import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.feature_selection import VarianceThreshold

ds = load_iris()

x =ds.data
y =ds.target

#plt.plot(x)
x.var(axis = 0)

Vselec = VarianceThreshold(threshold = 0.5)
Vselec.fit_transform(x)
Vselec.get_support()

ds