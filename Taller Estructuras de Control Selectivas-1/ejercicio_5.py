#entradas
a=int(input("ingrese la cantidad que gano por las ventas el departamento 1: "))
b=int(input("ingrese la cantidad que gano por las ventas el departamento 2: "))
c=int(input("ingrese la cantidad que gano por las ventas el departamento 3: "))
d=int(input("ingrese el sueldo de los vendedores: "))
#caja negra
x=(a+b+c)*0.33
if a>x: 
    v1=d+d*0.20
else:
    v1=d
if b>x: 
    v2=d+d*0.20
else:
    v2=d
if c>x: 
    v3=d+d*0.20
else:
    v3=d
#salidas
print("el sueldo del vendedor 1 a fin de mes es de: ",v1)
print("el sueldo del vendedor 2 a fin de mes es de: ",v2)
print("el sueldo del vendedor 3 a fin de mes es de: ",v3)