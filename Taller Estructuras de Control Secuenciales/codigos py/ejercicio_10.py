#entradas
ca=int(input("digite la cantidad de chelines austriacos "))
dg=int(input("digite la cantidad de dracmas griegos "))
p=int(input("digite la cantidad de pesetas "))
#caja negra
A=(ca*956871)/100
B=(dg*88607)/100
C=B/20110
D=p/122499
E=(p*100)/9289
#salidas
print("la cantidad de chelines austriacos en pesetas es: ", A)
print("la cantidad de dracmas griegos en francos franceses es: ", C)
print("la cantidad de pesetas en dolares es: ", D )
print("la cantidad de pesetas en liras italianas es: ", E)
