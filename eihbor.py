import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

data_set = pd.read_excel('data_set/titanic3 (3) (1) - Copie.xls')
data_set.head()

# data data analys and editing
data_set = data_set.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'],axis=1)
data_set.dropna(axis= 0, inplace= True)
data_set['sex'].replace(['female','male'],[0,1],inplace = True)
data_set.head()

# data processin and modeling

for cross in range(1,10):
    model = KNeighborsClassifier(n_neighbors=cross) 
    print("model with 1 neighbors")
    x = data_set.drop('survived',axis=1)
    y = data_set["survived"]
    model.fit(x,y)
    model.score(x,y)
    data = model.score(x,y)*100
    if data >= 83.5:
        print('le bon score est :',data,'%')
        break

model.predict(x)
plt.hist(model.predict(x))