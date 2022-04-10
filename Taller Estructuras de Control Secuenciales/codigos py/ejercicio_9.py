#entradas
numero_horas_trabajadas=int(input("ingrese el numero de horas trabajadas "))
precio_por_hora=int(input("ingrese el precio por hora "))
#caja negra
salario=numero_horas_trabajadas*precio_por_hora
salario_neto=salario-(salario*0.20)
#salidas
print("el salario neto es: ", salario_neto)