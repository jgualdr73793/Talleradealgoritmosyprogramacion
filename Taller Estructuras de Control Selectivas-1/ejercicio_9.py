#entradas
a=str(input("ingrese su nombre completo "))
b=int(input("ingrese la cantidad del monto de la compra "))
#caja negra
if b<50000:
    x=b
    d=0
if b>=50000 and b<100000:
    x=b-(b*0.05)
    d=5
if b>=100000 and b<700000:
    x=b-(b*0.11)
    d=11
if b>=700000 and b<1500000:
    x=b-(b*0.18)
    d=18
if b>1500000:
    x=b-(b*0.25)
    d=25
#salidas
print(a)
print("el monto de la compra es de: ",b)
print("el monto a pagar es de: ",x )
print("el descuento recibido es de: ",d )