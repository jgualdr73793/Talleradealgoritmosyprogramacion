#entradas
c_p1=int(input("ingrese calificacion parcial 1 "))
c_p2=int(input("ingrese calificacion parcial 2 "))
c_p3=int(input("ingrese calificacion parcila 3 "))
c_ef=int(input("ingrse calificacion del examen final "))
c_pf=int(input("ingrese calificacion proyecto final "))
#caja negra
promedio_Calif_P=(c_p1+c_p2+c_p3)/3
Porcentaje_Calif_P=promedio_Calif_P*0.55
porcentaje_Calif_ef=c_ef*0.30
porcentaje_Calif_pf=c_pf*0.15
Calif_total=Porcentaje_Calif_P+porcentaje_Calif_ef+porcentaje_Calif_pf
#salidas
print("la calificacion total es: ", Calif_total)
