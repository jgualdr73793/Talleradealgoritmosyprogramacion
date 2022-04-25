#entradas
A=int(input("ingrese un digito para A "))
B=int(input("ingrese un digito para B "))
C=int(input("ingrese un digito para C "))
D=int(input("ingrese un digito para D "))
#caja negra 
x=(A*1000)+(B*100)
y=(C*10)+D
if y>=60:
    z=x+100
else:
    z=x
#salidas
print("el entero positivo N redondeado es: ",z)
