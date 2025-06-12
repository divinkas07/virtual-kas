import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score , validation_curve,GridSearchCV
from sklearn.metrics import confusion_matrix


iris = load_iris()
X = iris.data
Y = iris.target 

# visualisatoin des donnes
#plt.scatter(X[:,1],X[:,0],c=Y)
#sns.jointplot( x = X[:,1], y = X[:,0], data = iris , hue = Y)

# data processing 
x_train,x_test , y_train,y_test = train_test_split(X,Y, test_size = 0.2 , random_state = 2)

print('train set', x_train.shape)
print('test set 2', x_test.shape )

# new data processing 
#training data  
#sns.jointplot(x = x_train[:,0] , y = x_train[:,1] , data = iris, hue = y_train,)
# testing data 
#sns.jointplot(x = x_test[:,0] , y = x_test[:,1] , data = iris, hue = y_test)

# training process

model = KNeighborsClassifier(n_neighbors = 1)
model.fit(x_train,y_train)
data = model.score(X,Y)
#print(data*100,"%")

# corss validation 
cross_val_score(KNeighborsClassifier(),x_train,y_train, cv = 5, scoring='accuracy').mean()

# validation curve
p = np.arange(1,50)
T_score , V_score  = validation_curve(KNeighborsClassifier(n_neighbors = 14),x_train,y_train,param_name ='n_neighbors',param_range = p ,cv = 5)

print(T_score.mean(axis = 1))
#plt.plot(p,V_score.mean(axis = 1),label = "validation_score")
#plt.plot(p,T_score.mean(axis=1),label="training_score")
#plt.legend()
#plt.show

#gridsarcheCV
p_grid = {"n_neighbors": np.arange(1,50),'metric':['euclidean','manhattan']}
 
grid = GridSearchCV(KNeighborsClassifier(3),p_grid,cv = 5)

t1 = grid.fit(x_train,y_train)

grid.best_score_
grid.best_params_
model2 = grid.best_estimator_
model2.score(X,Y) 
prd = confusion_matrix(y_test,model2.predict(x_test))
#sns.heatmap(prd)
 
# courbe d'aprentissage
V , Train_score , Test_score = learning_curve(model2,x_train,y_train, train_sizes= np.linspace(0.1,1.0,10), cv = 5 )

plt.plot(V, Train_score.mean(axis=1),'--', label='train score')
plt.plot(V, Test_score.mean(axis=1),'-',label='validation score')
plt.legend()
plt.show()