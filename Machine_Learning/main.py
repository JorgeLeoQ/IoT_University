import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

acc = linear.score(x_test, y_test)

print(acc)

#this in 5-dimesnional so in this case we had 5 coefficent
print("Co: \n",linear.coef_)
print("Inercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])