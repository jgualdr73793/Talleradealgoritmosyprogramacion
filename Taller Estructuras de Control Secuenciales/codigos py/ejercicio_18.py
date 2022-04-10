#entradas
bolivaresx=int(input("ingrese la cantidad de bolivares que se prestaron "))
bolivaresy=int(input("ingrese la cantidad de bolivares que se pagaron de interes en 4 años "))
#caja negra
razon=(bolivaresy*100)/(bolivaresx*4)
#salidas
print("el porcentaje que se cobraron por el prestamo fue: ", razon)
