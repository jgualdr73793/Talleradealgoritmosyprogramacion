#entradas
PVP=int(input("ingrese el precio del producto sin descuento "))
PVF=int(input("ingrse el precio a pagado por el producto con el descuento "))
#caja negra
descuento=100-((PVF*100)/PVP)
#salidas
print("el porcentaje del descuento hecho al producto es de: ", descuento)
