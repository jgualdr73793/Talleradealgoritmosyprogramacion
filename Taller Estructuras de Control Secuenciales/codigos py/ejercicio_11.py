#entradas
nombre=input("ingrese su nombre ")
pago_por_hora=int(input("ingrese el pago por hora "))
horas_extra=int(input("ingrese la cantidad de horas extra "))
Aa=int(input("ingrese la cantidad de actualizaciones academicas "))
CH=int(input("ingrese la cantidad de hijos que tiene "))
h=int(input("ingrese la cantidad de hogares que tiene "))
horasnt=int(input("ingrese la cantidad de horas normales trabajadas al dia "))
#caja negra
PHorasE=horas_extra*(pago_por_hora+(pago_por_hora*0.25))
sueldo_base=horasnt*pago_por_hora
deducciones=sueldo_base-(sueldo_base*0.14)
A_aca=Aa*250000
C_hijos=CH*173000
C_horas=h*180000
asignaciones=A_aca+C_hijos+C_horas
sueldo_neto=sueldo_base+PHorasE-deducciones
snD=sueldo_neto*31
#salidas
print("las asignaciones conrresponden a: ", asignaciones)
print("las deducciones conrresponden a: ", deducciones)
print("el sueldo neto para el mes de diciembre es: ", snD) 