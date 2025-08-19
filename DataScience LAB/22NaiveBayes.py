from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
iris= load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_n=GaussianNB()
c_n.fit(x_train,y_train)
y_pred=c_n.predict(x_test)
print("Accuracy :",metrics.accuracy_score(y_test,y_pred))
print("enter the sample data")
a=int(input("sepal length:"))
b=int(input("sepal width:"))
c=int(input("petal length:"))
d=int(input("petal width:"))
sample=[[a,b,c,d]]
pred=c_n.predict(sample)
pred_v=[iris.target_names[p]for p in pred]
print(pred_v)
