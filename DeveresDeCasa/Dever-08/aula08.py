from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X = iris.data
y = iris.target
nomes = iris.target_names

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X,y)

sepal_lenght = float(input('Digite o sepal lenght: '))
sepal_width = float(input('Digite o sepal width: '))
petal_lenght = float(input('Digite o petal lenght: '))
petal_width = float(input('Digite o petal width: '))

nova_flor = [[sepal_lenght, sepal_width, petal_lenght, petal_width]]
predicao  = modelo.predict(nova_flor)

print(f"\nA flor é {nomes[predicao[0]]}")