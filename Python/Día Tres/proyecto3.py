print("""¡Hola! Este es un analizador de texto profesional""")

texto = input("Por favor introduce el texto a analizar: ").lower()
print("Ahora por favor elige 3 letras al azar:")

letra1 = input("Introduce la primera letra: ").lower()
letra2 = input("Introduce la segunda letra: ").lower()
letra3 = input("Introduce la tercera letra: ").lower()

letras = [letra1, letra2, letra3]

contar1 = texto.count(letra1)
contar2 = texto.count(letra2)
contar3 = texto.count(letra3)

print(f"El texto ' {texto} ' tiene {contar1} letras '{letra1}', {contar2} letras '{letra2}' y {contar3} letras '{letra3}'.")

palabras = texto.split()
print(f"Tu texto tiene un total de {len(palabras)} palabras.")

print(f"La primer palabra de tu texto es {palabras[0]} y la ultima {palabras[-1]}")

palabras_al_reves = palabras[::-1]
print(f"El texto se vería así al reves: {' '.join(palabras_al_reves)}")

print(f"¿La palabra Python se encuentra en el texto? {'python' in texto.lower()}")
