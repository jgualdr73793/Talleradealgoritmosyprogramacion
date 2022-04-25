#entradas
a=int(input("ingrese el sueldo bruto del trabajador "))
#caja negra
if a>=5000000:
    c=1
if a>=4300000 and a<5000000:
    c=2
if a>=3600000 and a<4300000:
    c=3
if a>=2000000 and a<3600000:
    c=4
if a>=900000 and a<2000000:
    c=5
if c==1:
    Sa=a+(a*0.10)
if c==2:
    Sa=a+(a*0.15)
if c==3:
    Sa=a+(a*0.20)
if c==4:
    Sa=a+(a*0.40)
if c==5:
    Sa=a+(a*0.60)
# salidas
print("el nuevo sueldo bruto del trabajador es de: ", Sa)
print("la categoria del trabajador es de: ", c)