# Los Strings son un tipo de dato formato por cadenas de texto o secuencias de caracteres de cualquier tipo formando un texto
# Los Strings son inmutables, lo que significa que no se pueden cambiar una vez creados 

# Se pueden definir utilizando comillas simples o dobles
mi_string = "Hola, mundo \"Hola\"!"
mi_string2 = 'Esto es parte de un string'



mi_string3 = mi_string + " " + mi_string2

print(mi_string3)
print("Esta es una línea \ny esta es otra línea.")
print("\tEsta es una línea y esta es otra línea.")
print("This isn\'t a number")
print("Este signo \\ es una barra invertida")


# Ejercicio 1: Concatenar dos strings y mostrarlos
saludo = "Hola"
nombre = "Ana"
mensaje = saludo + ", " + nombre + "!"
print(mensaje)

# Ejercicio 2: Usar caracteres de escape para mostrar comillas dentro de un string
frase = "Ella dijo: \"Python es divertido!\""
print(frase)

# Ejercicio 3: Mostrar un string en varias líneas usando \n
multilinea = "Primera línea\nSegunda línea\nTercera línea"
print(multilinea)

# Ejercicio 4: Mostrar una tabulación usando \t
tabulado = "Nombre:\tJuan"
print(tabulado)

# Ejercicio 5: Mostrar una barra invertida
barra = "Ruta: C:\\Users\\Ana"
print(barra)
