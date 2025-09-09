import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('tshirt.csv')
X = df[['Height', 'Weight']]
y = df['T_Shirt_Size']
#row1=df.iloc[1:]
#print(row1)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
a = int(input("Enter height: "))
b = int(input("Enter weight: "))
sample = [[a, b]]
predicted_size = knn.predict(sample)
print(f"The predicted t-shirt size is: {predicted_size[0]}")
