#entradas
mujeres=int(input("ingrese la cantidad de mujeres: "))
hombres=int(input("ingrese la cantidad de hombres: "))
#caja negra
cantidad_de_personas=mujeres+hombres
mh=round((mujeres*100)/cantidad_de_personas)
hh=round((hombres*100)/cantidad_de_personas)
#salidas
print("la cantidad de mujeres es:", mh)
print("la cantidad de hombres es: ", hh)