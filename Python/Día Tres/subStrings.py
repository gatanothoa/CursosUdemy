 #Extraer Sub-Strings

# Extraer sub-strings significa obtener partes de una cadena de texto.
# En Python, se hace usando la notación de slicing: cadena[inicio:fin]
# Ejemplo:
texto = "Python es divertido"
subcadena = texto[7:9]  # Extrae los caracteres desde la posición 7 hasta la 8 (no incluye la 9)
print(subcadena)  # Imprime: es

texto = "ABCDEFGHIJKLM"
subcadena = texto[2:5]  # Extrae los caracteres desde la posición 2 hasta la 4 (no incluye la 5)
print(subcadena)  # Imprime: CDE

print(texto[1:10:3])  # Imprime: BDFHJL
