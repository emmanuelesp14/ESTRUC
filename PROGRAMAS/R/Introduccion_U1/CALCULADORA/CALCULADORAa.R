# Función para realizar la suma de dos números
sumar <- function(a, b) {
  return(a + b)
}

# Función para realizar la resta de dos números
restar <- function(a, b) {
  return(a - b)
}

# Función para realizar la multiplicación de dos números
multiplicar <- function(a, b) {
  return(a * b)
}

# Función para realizar la división de dos números
dividir <- function(a, b) {
  if (b == 0) {
    return("Error: No se puede dividir por cero")
  }
  return(a / b)
}

# Menú de la calculadora
while (TRUE) {
  cat("Opciones:\n")
  cat("1. Sumar\n")
  cat("2. Restar\n")
  cat("3. Multiplicar\n")
  cat("4. Dividir\n")
  cat("5. Salir\n")
  
  opcion <- as.numeric(readline("Selecciona una opción: "))
  
  if (opcion == 5) {
    break
  }
  
  if (opcion >= 1 && opcion <= 4) {
    num1 <- as.numeric(readline("Ingresa el primer número: "))
    num2 <- as.numeric(readline("Ingresa el segundo número: "))
    
    if (opcion == 1) {
      resultado <- sumar(num1, num2)
    } else if (opcion == 2) {
      resultado <- restar(num1, num2)
    } else if (opcion == 3) {
      resultado <- multiplicar(num1, num2)
    } else if (opcion == 4) {
      resultado <- dividir(num1, num2)
    }
    
    cat("Resultado: ", resultado, "\n")
  } else {
    cat("Opción no válida\n")
  }
}
