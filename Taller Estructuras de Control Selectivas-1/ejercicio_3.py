#entradas
A=int(input("digite valor de A "))
B=int(input("digite valor de B "))
C=int(input("digite valor de C "))
D=int(input("digite valor de D "))
#caja negra
if D==0:
    x=(A-C)**2
if D>0:
    x=((A-B)**3)/D
#salidas
print(x)