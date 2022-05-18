ejemplo=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64,23]
resultado={}
coleccion=set(ejemplo)
print(coleccion)
for i in coleccion:
    diccionario={
        i:ejemplo.count(i)
    }
    resultado.update(diccionario)
print(resultado)
