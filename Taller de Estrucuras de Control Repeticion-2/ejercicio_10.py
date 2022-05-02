x=int(input("ingrese la cantidad de estudiantes "))
c=0
lista=[]
while c<x:
    c+=1
    a=float(input("ingrese su estatura "))
    lista.append(float(a))
    if c==x:
        r=max(lista,key=float)
        print("la estatura mayor es de: ",r)
