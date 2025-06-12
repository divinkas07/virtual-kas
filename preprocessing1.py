import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
from sklearn.preprocessing  import *
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
ds = pd.read_excel('data_set/titanic3 (3) (1) - Copie.xls')
ds.head()

# data process 1 

data = ds.drop(['name','sibsp','parch','ticket','fare','cabin','embarked',	'boat',	'body',	'home.dest'],axis = 1) 
data.dropna(inplace= True)
data['sex'].replace(['female','male'],[0,1], inplace= True) 
data.head()
#sns.pairplot(data , hue ='survived')
# data test data train

X = data.drop(['survived'],axis=1) 
Y = data['survived']
X,Y
x_train,x_test,y_train,y_test = train_test_split(X,Y , test_size= 0.2, random_state=5)

# data transformations

model = make_pipeline(                      
                     
                     StandardScaler(), 
                     KNeighborsClassifier(),                    
                     )

#dic = {'n_neighbors':np.arange(0,100),'metrics':['manhattan','euclidean']}
#drg = GridSearchCV(model, dic,cv=5)
model.fit(x_train,y_train)
model.score(x_train,y_train)
srt = model.predict(x_test) 
sns.heatmap(srt)