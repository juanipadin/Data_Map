import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

boston = datasets.load_boston()
print (boston)
print()
print (boston.keys())
print ()
print (boston.DESCR)
print()
print(boston.feature_names)

X= boston.data[:,np.newaxis,5]
Y= boston.target

plt.scatter(X,Y)
plt.xlabel('Numero de habitaciones')
plt.ylabel('Valor medio')
plt.show()


from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

lr = linear_model.LinearRegression()

lr.fit (X_train, Y_train)

Y_pred = lr.predict(X_test)

plt.scatter(X_test,Y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title ('Regresion Lineal Simple')
plt.xlabel ('Numero de habitaciones')
plt.ylabel('Valor medio')
plt.show()

print()
print('DATOS DEL MODELO REGRESION SIMPLE')
print ()
print ('Valor de la prediccion o coeficiente "a": ')
print (lr.coef_)
print ()
print('Valor de la interseccion o coeficiente "b": ')
print (lr.intercept_)
print ()
print('La ecuacion del modelo es igual a: ')
print ('y= ', lr.coef_, 'x ', lr.intercept_)

print ()
print ('Presicion del modelo:')
print(lr.score(X_train, Y_train))
