#entradas
X=int(input("ingrese la cantidad de naranjas "))
Y_Bs=int(input("ingrese la cantidad de bolivares por docena "))
K=int(input("ingrese la cantidad de bolivares obtenidos "))
#caja negra
A=(X/12)*Y_Bs
diferencia=(K-A)
ganancia= (diferencia*100)/A
#salidas
print("el porcentaje de ganancia es de: ", ganancia)