import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn import metrics

from sklearn.neighbors import KNeighborsclassifier

df = pd.read_csv('tshirt.csv')

X = df.iloc[:, :-1]

y = df.ilocf:, -11

1 print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

16 knn = KNeighborsclassifier(n_neighbors 17 knn.fit(X_train, y train)

19 y_pred = knn.predict(X test)

1 print("accuracy:", metrics.accuracy_score(y_test, y_pred))

int(input('Enter height

int(input('Enter weight

samples = pd.DataFrame({'height

[h], weight: [w]})

25

27 pred_v = knn.predict(samples)

28 print(pred_v)
