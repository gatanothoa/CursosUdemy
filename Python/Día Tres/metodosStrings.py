texto = "Este es el texto de Emmanuel"
resultado = texto.upper()  # Convierte todo el texto a mayúsculas
resultado1 = texto.lower()  # Convierte todo el texto a minúsculas
resultado2 = texto[2].upper()  # Convierte el tercer carácter a mayúsculas
resultado3 = texto.split() # Divide el texto en una lista de palabras
resultado4 = texto.split("t") # Divide el texto en una lista de palabras usando "t" como separador
resultado5 = texto.find("Emmanuel")  # Encuentra la posición de "Emmanuel" en el texto
resultado6 = texto.replace("Emmanuel", "Juan")  # Reemplaza "Emmanuel" con "Juan"

a = "Aprender"
b = "programación"
c = "es divertido"
d = " ".join([a, b, c])  # Une las palabras con un espacio entre ellas


print(resultado)
print(resultado1)  # Imprime: este es el texto de emmanuel
print(resultado2)  # Imprime: T
print(resultado3)  # Imprime: ['Este', 'es', 'el', 'texto', 'de', 'Emmanuel']
print(resultado4)  # Imprime: ['Es', 'e', 'e', 'e', 'o', 'Emanuel']
print(d)  # Imprime: Aprender programación es divertido
print(resultado5)  # Imprime: 20 (posición de "Emmanuel" en el texto)
print(resultado6)  # Imprime: Este es el texto de Juan

# Ejercicios sin resolver:

# 1. Convierte solo la primera letra de cada palabra en mayúscula en el texto.
resultado7 = texto.title()  # Convierte la primera letra de cada palabra a mayúscula
print(resultado7)  # Imprime: Este Es El Texto De Emmanuel


