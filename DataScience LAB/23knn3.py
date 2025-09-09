import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv('Food.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
row1=df.iloc[0:]
print(row1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
h = int(input('Enter Sweetness: '))
w = int(input('Enter Crunchiness: '))
samples = pd.DataFrame({'Sweetness': [h], 'Crunchiness': [w]})

pred_v = knn.predict(samples)
print("Predicted class:", pred_v[0])
