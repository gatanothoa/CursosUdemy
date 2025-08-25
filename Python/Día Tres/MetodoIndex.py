#Método index()
"""
El método `index()` en Python se utiliza para buscar la primera aparición de un elemento especificado dentro de una secuencia, como una lista o una cadena. Retorna el índice (posición) del elemento encontrado. Si el elemento no existe en la secuencia, se lanza una excepción `ValueError`. Opcionalmente, se pueden especificar los parámetros `start` y `end` para limitar el rango de búsqueda.
"""

mi_texto = "Esta es una prueba"
resultado = mi_texto[9]
resultado1 = mi_texto.index("a",5)
resultado2 = mi_texto[-1]
resultado3 = mi_texto.rindex("a")


print(resultado)
print(resultado1)    
print(resultado2)
print(resultado3) 

# Ejercicios para practicar el método index()

# 1. Encuentra el índice de la primera aparición de la letra "e" en la cadena mi_texto.
resultado4 = mi_texto.index("e")
print(f"1. Índice de la primera 'e': {resultado4}")

# 2. Busca el índice de la palabra "prueba" en mi_texto usando index().
resultado5 = mi_texto.index("prueba")
print(f"2. Índice de la palabra 'prueba': {resultado5}")

# 3. ¿Qué sucede si buscas una letra que no existe? Prueba buscar "z" y maneja la excepción.
try:
    resultado6 = mi_texto.index("z")
except ValueError:
    print("3. No se encontró la letra 'z' (ValueError)")

# 4. Utiliza index() para buscar la letra "s" comenzando desde el índice 5.
resultado7 = mi_texto.index("s", 5)
print(f"4. Índice de la letra 's' desde el índice 5: {resultado7}")

# 5. Usa rindex() para encontrar la última aparición de la letra "e".
resultado8 = mi_texto.rindex("e")
print(f"5. Última aparición de la letra 'e': {resultado8}")
