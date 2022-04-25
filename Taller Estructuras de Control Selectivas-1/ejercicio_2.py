#entradas
x=int(input("ingrese el sueldo del trabajador "))
#caja negra 
if x<900000:
    b=x+(x*0.15)
else: 
    b=x+(x*0.12)
#salidas
print("el nuevo sueldo del trabajador es de:  ", b)

