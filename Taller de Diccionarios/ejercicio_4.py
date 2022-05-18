x=int(input("ingrese la cantidad de estudiantes "))
lista_a=[]
lista_s=[]
notas=[]
estudiantes={}
for c in range(1,x+1,1):
    ne=input("ingrese nombre del estudiante ")
    no=float(input("ingrese la nota del estudiante "))
    estudiantes.update({c:{"nombre":ne, "nota":no}})
for i in estudiantes.keys():
    if (estudiantes[i]["nota"])<=5:
            lista_s.append(estudiantes[i]["nombre"])
    if (estudiantes[i]["nota"])>5:
        lista_a.append(estudiantes[i]["nombre"])
    notas.append(estudiantes[i]["nota"])
media=(sum(notas))/x
print("el/los estudiante/s que suspendio/dieron fue/ron: ",lista_s)
print("el/los estudiante/s que aprobo/baron fue/ron: ",lista_a)
print("el promedio de notas es de: ",media)



