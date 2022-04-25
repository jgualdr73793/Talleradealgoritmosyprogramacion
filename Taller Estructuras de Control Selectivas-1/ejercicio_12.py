#entradas
a = int (input ('Ingresa la cantidad entera de dinero en COP: '))
#caja negra
b=a
c1=(b-b%100000)//100000
b=b%100000
c2=(b-b%50000)//50000
b=b%50000
c3=(b-b%20000)//20000
b=b%20000
c4=(b-b%10000)//10000
b=b%10000
c5=(b-b%5000)//5000
b=b%5000
c6=(b-b%2000)//2000
b=b%2000
c7=(b-b%1000)//1000
b=b%1000
c8=(b-b%500)//500
b=b%500
c9=(b-b%200)//200
b=b%200
c10=(b-b%100)//100
b=b%100
c11=(b-b%50)//50
#salidas
print("la cantidad de billetes de 100000 es: ",c1)
print("la cantidad de billetes de 50000 es: ",c2)
print("la cantidad de billetes de 20000 es: ",c3)
print("la cantidad de billetes de 10000 es: ",c4)
print("la cantidad de billetes de 5000 es: ",c5)
print("la cantidad de billetes de 2000 es: ",c6)
print("la cantidad de billetes de 1000 es: ",c7)
print("la cantidad de monedas de 500 es: ",c8)
print("la cantidad de monedas de 200 es: ",c9)
print("la cantidad de monedas de 100 es: ",c10)
print("la cantidad de monedas de 50 es: ",c11)
