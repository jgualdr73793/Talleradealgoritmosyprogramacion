#entradas
N1=int(input("ingrese la cantidad de billetes de 50000 "))
N2=int(input("ingrese la cantidad de billetes de 20000 "))
N3=int(input("ingrese la cantidad de billetes de 10000 "))
N4=int(input("ingrese la cantidad de billetes de 5000 "))
N5=int(input("ingrese la cantidad de billetes de 2000 "))
N6=int(input("ingrese la cantidad de billetes de 1000 "))
N7=int(input("ingrese la cantidad de billetes de 500 "))
N8=int(input("ingrese la cantidad de billetes de 100 "))
#caja negra
A=N1*50000
B=N2*20000
C=N3*10000
D=N4*5000
E=N5*2000
F=N6*1000
G=N7*500
H=N8*100
dinero_total=A+B+C+D+E+F+G+H 
#salidas
print("la cantidad de dinero en el banco es de: ", dinero_total)
