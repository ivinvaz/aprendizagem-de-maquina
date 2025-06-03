from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn import metrics
import pandas as pd

massData = pd.read_csv("./Advertising.csv", index_col=0)
reglin = LinearRegression()

X = massData[["TV","radio","newspaper"]]
y = massData["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


reglin.fit(X_test, y_test)
print(reglin.coef_)

previsoes = logReg.predict(X_test)
print ((metrics.mean_squared_error (y_test, previsoes))** 0.5)