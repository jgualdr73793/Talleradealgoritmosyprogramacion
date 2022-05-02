xy=input()
x,y=xy.split(" ")
x=int(x)
y=int(y)
z=x-y
lista=[z]
while z>0:
    z-=y
    lista.append(z)
print("el resto de la division es: ",z)
print("la cantidad de restas efectuadas es de: ",len(lista))
