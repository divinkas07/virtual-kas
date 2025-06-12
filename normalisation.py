import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import*
from sklearn.pipeline import make_pipeline



iris = load_iris()
X = iris.data
Y = iris.target 


#set
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2, random_state= 5)
#plt.scatter(x_train[:,1],x_train[:,0] ,c=y_train)
#plt.scatter(y_train[:,1],y_train[:,0] ,c=x_train)
# model

model = make_pipeline( StandardScaler(),
                      SGDClassifier())


model.fit(x_train,y_train)
model.score(x_train,y_train)



xt,yt,data = learning_curve(model, x_train, y_train, train_sizes= np.linspace(0.1,1.0,10), cv = 5)

plt.plot(xt, label ='xt training')

plt.plot(yt,label ='yt training',color = 'yellow')
plt.plot(data, label = 'data add', color= 'red' )
plt.subplot()

plt.show