#entradas
a=int(input("ingrese la lectura anterior en kilovatios/hora "))
b=int(input("ingrese la lectura actual en kilovatios/hora "))
#caja negra
x=b-a
if x<=100:
    p=4600
if 100<x<=300:
    p=80000
if 300<x<=500:
    p=100000
if x>500:
    p=120000
#salidas
print("el monto a pagar es de:",p )