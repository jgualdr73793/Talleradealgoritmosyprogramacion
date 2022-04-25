#entradas
x=int(input("ingrese la cantidad de dinero invertido en el banco "))
y=int(input("ingrese el porcentaje que paga el banco por interes al mes "))
#caja negra y salidas
A=(x*(y/100))/12
B=x+A
if A>100000:
    print("La cantidad de dinero en la cuenta es de: ", B)
else:
    print("la canridad de dinero en la cuenta es de: ", x)