import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import*




data_set = pd.read_excel('data_set/titanic3 (3) (1) - Copie.xls')
data_set.head()

# data_set
data_set = data_set.drop(['name','sibsp','parch','ticket','fare','cabin','boat','body','home.dest'],axis=1)
data_set.dropna(axis= 0, inplace= True)
  
data_set.head()
x = data_set.drop("survived", axis=1)
y = data_set['survived']

#train_test_set...
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state= 2)

# data preprocessing

# encodage 
encoder = OrdinalEncoder()
encoder.fit_transform(x_train)


