#entradas
K=int(input("ingrese el valor de K menor que N "))
N=int(input("ingrese el valor de N mayor que K "))
#caja negra
print(N)
while K<N:
    N-=1
    print(N)
    if K==N:
        break
     
