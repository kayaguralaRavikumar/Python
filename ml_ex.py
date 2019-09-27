from sklearn.neighbors import KNeighborsClassifier as kn
import pandas as pd
from sklearn.metrics import accuracy_score as acc

knn = kn()
df = pd.read_csv('iris.csv')
x = df.iloc[:, 0:4]
y = df.iloc[:, 4]

knn.fit(x, y)

r1 = knn.predict([[3, 5, 4, 2]])

print('r1=', r1)

# accuracy
# 1 -way
r2 = knn.predict(x)
a1 = acc(r1, y)
print('a1=', a1)

# 2 - way
from sklearn.model_selection import train_test_split as tts

x_train, y_train, x_test, y_test = tts(x, y)

k2 = kn()
k2.fit(x_train, y_train)
r3 = k2.predict(x_test)
a2 = acc(r3, y_test)

print('a1=', a2)
