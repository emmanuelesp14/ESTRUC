Algoritmo calcular_edad
	Definir año, edad Como Entero
	Escribir "INGRESA EL AÑO DE NACIMIENTO"
	Leer año
	edad <- 2023 - año
	Escribir "LA PERSONA TIENE" edad "AÑOS"
	Si (edad >=18) Entonces
		Escribir "ES MAYOR DE EDAD Y SE PUEDE CASAR"
	SiNo
		Escribir "ES MENOR DE EDAD Y NO SE PUEDE CASAR"
	FinSi
FinAlgoritmo
