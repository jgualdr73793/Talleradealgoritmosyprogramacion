Algoritmo operaciones
	escribir "ingrese su nombre"
	leer nombre 
	escribir "ingrese su primer apellido"
	leer primerapellido
	escribir "ingrese su segundo apellido" 
	leer segundoapellido
	primerletra<-subcadena(nombre, 1,1)
	segundaletra<-subcadena(primerapellido,1,1)
	terceraletra<-subcadena(segundoapellido,1,1)
	escribir "las iniciales son:" Mayusculas(primerletra) Mayusculas(segundaletra) Mayusculas(terceraletra)
FinAlgoritmo
