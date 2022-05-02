x=0
for c in range(97,1004,1):
    if c%2==0:
        x=x+c
        if c==1002:
            print(x)