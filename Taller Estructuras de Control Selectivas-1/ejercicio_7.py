#entradas
a=int(input("ingrese la cantidad de km recorridos "))
b=int(input("ingrese la cantidad de km adicionales "))
#caja negra
if a<300:
    b=50000
if a>=300 and a<1000:
    b=70000+b*30000
if a>=1000:
    b=150000+b*9000
#salidas
print("el valor a pagar por el cliente es de: ",b)