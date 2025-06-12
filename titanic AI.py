import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,learning_curve
from sklearn.metrics import confusion_matrix


data_set = pd.read_excel('data_set/titanic3 (3) (1) - Copie.xls')
data_set.head()

# data_set
data_set = data_set.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'],axis=1)
data_set.dropna(axis= 0, inplace= True)
data_set['sex'].replace(['female','male'],[0,1],inplace = True)
data_set.head()
x = data_set.drop("survived", axis=1)
y = data_set['survived']

#train_test...
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state= 2)
x_train,y_train, x_test,y_test

vc = cross_val_score(KNeighborsClassifier(),x_train,y_train,cv=5,scoring='accuracy').mean()
#pre-entrainement et calcul

G_d = {'n_neighbors':np.arange(0,50),'metric':['eucludean','manhattan'] }
G_model = GridSearchCV(KNeighborsClassifier(),G_d,cv=5)
G_model.fit(x_train,y_train)
G_model.best_score_
G_model.best_params_
model = G_model.best_estimator_
#print(G_model.predict(x_train))
pt = confusion_matrix(y_test,model.predict(x_test))

#sns.heatmap(pt)
pt
model.score(x_test,y_test)

# learnig curve
Nt , t_score,v_score = learning_curve(model,x_train,y_train, train_sizes= np.linspace(0.1,1.0,10)) 

#plt.plot(Nt,v_score,label ='v_score')

def survi(model,PClass =2  ,age =18 ,sex = 1):
    x = np.array([PClass,age,sex]).reshape(1,3)
    print(model.predict(x))
    print(model.predict_proba(x))
    if model.predict(x) == 1 and sex == 1:
        print("haa selon mes analyse vous pourrait survecu a cette catastrophe monsieur")
        print("votre probabilité de survie est de : ",model.predict_proba(x)[0][1]*100,"%")
    elif model.predict(x) == 0 and sex == 1:
        print("désolé monsieur mais vous ne pourrait pas survecu a cette catastrophe")
        print("votre probabilité de survie est de : ",model.predict_proba(x)[0][1]*100,"%")
    elif model.predict(x) == 1 and sex == 0:
        print("haa selon mes analyse vous pourrait survecu a cette catastrophe madame")
        print("votre probabilité de survie est de : ",model.predict_proba(x)[0][1]*100,"%")
    elif model.predict(x) == 0 and sex == 0:
        print("désolé madame mais vous ne pourrait pas survecu a cette catastrophe")
        print("votre probabilité de survie est de : ",model.predict_proba(x)[0][1]*100,"%")
    else:
        print("désolé mais je ne peut pas faire des prédictions sur votre cas")
        print("votre probabilité de survie est de : ",model.predict_proba(x)[0][1]*100,"%")
    
   
survi(model)

                                                                                                                                                                                                                                                                                                                                                