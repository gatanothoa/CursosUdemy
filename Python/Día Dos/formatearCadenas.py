#Formatear Cadenas

# Formatear cadenas es el proceso de insertar valores dentro de una cadena de texto.
# En Python, esto se puede hacer usando f-strings, el método format() o el operador %.
# Ejemplo con f-string:
nombre = "Juan"
edad = 25
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)

# Ejemplo con el método format()
mensaje2 = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje2)

# Ejemplo con el operador %
mensaje3 = "Hola, mi nombre es %s y tengo %d años." % (nombre, edad)
print(mensaje3)