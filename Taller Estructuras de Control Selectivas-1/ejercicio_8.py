#entradas
P=int(input("ingrese el valor de P "))
Q=int(input("ingrese el valor de Q "))
#caja negra y salidas
a=(P,Q)
x=(P**3) + (Q**4)-(2*(P**2))
if x>680:
    print(a,"satisfacen la expresión ")
else:
    print(a,"no satisfacen la expresión ")