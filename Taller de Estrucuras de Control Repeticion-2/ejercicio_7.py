while True:
    XM=input()
    X, M=XM.split(" ")
    X=int(X)
    M=int(M)
    if (X == 0 and M == 0):
        break
    E=X*M
    print(E)