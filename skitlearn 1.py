import numpy as np
import matplotlib.pyplot as plt
import pandas as dp 
import seaborn as sns
from sklearn.linear_model import LinearRegression 

# generation aleatoir 
np.random.seed(0)
t = 200
x = np.linspace(1,11, t).reshape(t,1)
y = x + np.random.randn(t,1)
data = x.mean() + y.mean()**2

# exploit
plt.scatter(x,y,c=x)

#data processing and Ai

model = LinearRegression()
model.fit(x,y)
model.score(x,y)
pdr = model.predict(x)
plt.plot(x,pdr,c='r')