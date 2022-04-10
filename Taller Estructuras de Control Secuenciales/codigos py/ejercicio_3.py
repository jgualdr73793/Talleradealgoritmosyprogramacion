#entradas
sueldo_base=int(input("ingrese el sueldo base"))
#caja negra
comisiones=((sueldo_base*10)/100)
total_recibido=sueldo_base+comisiones
#salidas
print("las comisiones son: ", comisiones)
print("el total recibido es: ", total_recibido)
