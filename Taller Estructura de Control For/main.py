archivo = open("paises.txt","r")
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  print(a)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)
"""
#Cuente e imprima cuantas ciudades inician con la letra M
"""
lista=[]
ciudades=[]
c=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="M"):
    print(i)
    c+=1
print(c)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
for i in archivo:
  x,y=i.split(": ")
  x=str(x)
  y=str(y)
  if x[0]=="U":
    print(x)
  if y[0]=="U":
    print(y)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
c=0
for i in archivo:
  a=i.index(":")
  c+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
print(c)
"""
#Busque e imprima la ciudad de Singapur  
"""
for i in archivo:
  x,y=i.split(": ")
  x=str(x)
  y=str(y)
  if x!="Singapur":
    pass
  else:
    print(y)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
for i in archivo:
  x,y=i.split(": ")
  x=str(x)
  y=str(y)
  if x!="Venezuela":
    pass
  else:
    print(x)
    print(y)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
ciudades=[]
c=0
for i in archivo:
  x,y=i.split(": ")
  x=str(x)
  y=str(y)
  if x[0]!="E":
    pass
  else:
    ciudades.append(y)
    print(x)
    print (y)
print(len(ciudades))
"""
#Busque e imprima la Capital de Colombia
"""
for i in archivo:
  x,y=i.split(": ")
  x=str(x)
  y=str(y)
  if x!="Colombia":
    pass
  else:
    print(y)
"""
#imprima la posicion del pais de Uganda
"""
lista=[]
c=1
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
  if a!="Uganda":
    c+=1
  if a=="Uganda":
    break
print (c)
"""
#imprima la posicion del pais de Mexico
"""
lista=[]
c=1
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
  if a!="México":
    c+=1
  if a=="México":
    break
print (c)
"""
# alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
""""
paises=[]
for i in archivo:
  paises.append(i)
  if i=="Madagascar: rey julien\n":
    x=paises.index("Madagascar: rey julien\n")
    paises.remove("Madagascar: rey julien\n")
    paises.insert(x,"Madagascar: Antananarivo\n")
  a="".join(paises)
  print(a)
  paises=[]
"""
#Agregue un país que no esté en la lista
"""
pais = "Escocia: Edimburgo"
paises_2=open("paises.txt","a")
paises_2.write("\n"+pais+"\n")
paises_2.close()
#no pude ordenarlo de manera ascendente,quedo al final
"""
archivo.close()
