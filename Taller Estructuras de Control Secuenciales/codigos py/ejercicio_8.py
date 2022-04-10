import math
#entradas
a=float(input("ingrese lado a: "))
b=float(input("ingrse lado b: "))
c=float(input("ingrese lado c: "))
#caja negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#salidas
print("el area es: ",round(area,2))
