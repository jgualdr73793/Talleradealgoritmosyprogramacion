#entradas
a=input()
#caja negra
a1,a2,a3,a4=a.split(" ")
a1=int(a1)
a2=int(a2)
a3=int(a3)
a4=int(a4)
x=a4
suma=a1+a2+a3+a4
diferencia=a2-a1
diferencia=a4-a3
for an in range(1,9,1):
    if an<9:
        x+=diferencia
        suma+=x
        if an==9:
            break
#salidas
print("a12 es igual a: ", x)
print("la suma de los primeros 12 terminos es: ", suma)