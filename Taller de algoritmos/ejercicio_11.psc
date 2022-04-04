Algoritmo sin_titulo
	Calificacion_parcial_1<-A
	Calificacion_parcial_2<-B
	Calificacion_parcial_3<-C
	Calificacion_examen_final<-D
	Calificacion_proyecto_final<-E
	escribir "ingrese Calificacion parcial 1"
	Leer A
	escribir "ingrese Calificacion parcial 2"
	Leer B
	escribir "ingrese Calificacion parcial 3"
	leer C
	escribir "ingrese Calificacion examen final"
	leer D
	escribir "Calificacion proyecto final"
	leer E
	Total_calificaciones_parciales<-A+B+C
	escribir " el Total calificaciones parciales es: " Total_calificaciones_parciales
	promedio_calificaciones_parciales<-(Total_calificaciones_parciales)/3
	escribir "el promedio de calificaciones parciales es: " promedio_calificaciones_parciales
	x<-(promedio_calificaciones_parciales*55)/100
	Escribir "el 55% correspondiente a las calificacions parciales es: " x
	r<-(D*30)/100
	escribir "el 30% correspondiente a la calificacion del examen final es: " r 
	s<-(E*15)/100
	escribir "el 15% correspondiente a el proyecto final es: " s
	calificacion_total<-x+r+s
		escribir "la calificacion total es: " calificacion_total
FinAlgoritmo
