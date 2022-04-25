#entradas
a=int(input("ingrese el monto total de la compra "))
#caja negra y salidas
if a>5000000:
    x=a*0.55 
    y=a*0.30  
    z=a*0.15
    i=z*0.20
    print("la empresa invierte una cantidad de: ",x )
    print("la empresa pidio prestado al banco una cantidad de: ",y )
    print("la empresa solicito un credito al fabricante de: ",z )
    print("el monto a pagar por los intereses es de: ", i)
else:
    x=a*0.70
    y=a*0.30
    i=y*0.20
    print("la empresa invierte una cantidad de: ",x)
    print("la empresa solicita un credito al fabricante de: ",y)
    print("el monto a pagar por los intereses es de: ", i)
