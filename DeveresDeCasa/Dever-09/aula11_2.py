from sklearn.model_selection import KFold 
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
X, y = load_iris(return_X_y=True)
K = 5 

kf = KFold(n_splits=K, shuffle=True, random_state=42)
i =[]
for train_index, test_index in kf.split(X):
    X_treino, X_teste = X[train_index], X[test_index] 
    y_treino, y_teste = y[train_index], y[test_index]
    modelo = LogisticRegression() 
    modelo.fit(X_treino, y_treino)
    i.append(modelo.score(X_teste, y_teste))
print(sum(i)/len(i))