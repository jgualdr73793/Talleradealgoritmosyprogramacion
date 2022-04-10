#entradas
costo_por_kilovatio=int(input("ingrese el costo por kilovatio  "))
lectura_anterior=int(input("ingrese la lectura anterior en kilovatios "))
lectura_actual=int(input("ingrese la lectura actual en kilovatios "))
#caja negra
A=(lectura_actual-lectura_anterior)/costo_por_kilovatio
#salidas
print("el monto total a pagar es de: ", A)