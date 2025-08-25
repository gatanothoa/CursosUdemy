"""
Los strings en Python son secuencias inmutables de caracteres. Sus principales propiedades son:

- Inmutabilidad: Una vez creado, el contenido de un string no puede modificarse.
- Indexación: Se puede acceder a caracteres individuales mediante índices, empezando desde 0.
- Slicing: Se pueden obtener subcadenas usando la notación de slicing (string[inicio:fin]).
- Concatenación: Se pueden unir strings usando el operador +.
- Multiplicación: Se puede repetir un string usando el operador *.
- Métodos incorporados: Los strings tienen métodos útiles como .lower(), .upper(), .replace(), .split(), .join(), .find(), entre otros.
- Compatibilidad con Unicode: Los strings pueden contener cualquier carácter Unicode.
- Iterabilidad: Se puede iterar sobre los caracteres de un string usando bucles.
"""


# Ejemplo de indexación
texto = "Python"
print(texto[0])  # 'P'

# Ejemplo de slicing
print(texto[1:4])  # 'yth'

# Ejemplo de concatenación
saludo = "Hola"
nombre = "Mundo"
print(saludo + " " + nombre)  # 'Hola Mundo'

# Ejemplo de multiplicación
print("ha" * 3)  # 'hahaha'

# Ejemplo de métodos incorporados
print(texto.lower())  # 'python'
print(texto.upper())  # 'PYTHON'
print(texto.replace("P", "J"))  # 'Jython'
print(texto.split("t"))  # ['Py', 'hon']
print(" ".join(["uno", "dos", "tres"]))  # 'uno dos tres'
print(texto.find("th"))  # 2

# Ejemplo de iterabilidad
for letra in texto:
    print(letra)
