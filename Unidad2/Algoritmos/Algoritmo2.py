def invertir_frase(frase):
    # Dividir la frase en palabras
    palabras = frase.split()

    # Invertir el orden de las palabras
    palabras_invertidas = palabras[::-1]

    # Crear la frase invertida uniendo las palabras
    frase_invertida = ' '.join(palabras_invertidas)

    return frase_invertida

# Leer una frase desde la entrada estándar
frase = input("Ingrese una frase: ")

# Llamar a la función para invertir la frase
frase_invertida = invertir_frase(frase)

# Imprimir la frase invertida
print("Frase invertida:", frase_invertida)