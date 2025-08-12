# Conversiones entre tipos de datos

# Conversión implícita: Ocurre cuando Python convierte automáticamente un tipo de dato en otro sin intervención del programador.
# Conversión explícita: Ocurre cuando el programador indica explícitamente que desea convertir un tipo de dato en otro usando funciones como int(), float(), str(), etc.

num1 = 5
num2 = 2.5

num1 = num1 + num2  # Conversión implícita de int a float

print(type(num1))  # Imprime: <class 'int'>
print(type(num2))  # Imprime: <class 'float'>


num3 = float(input("Introduce un número: "))
print(type(num3))  # Imprime: <class 'float'>

num4 = int(num3)  # Conversión explícita de float a int
print(type(num4))  # Imprime: <class 'int'>

# Ejercicios sobre conversiones entre tipos de datos

# 1. Pide al usuario dos números enteros, súmalos y muestra el resultado como float.
num_a = int(input("Introduce el primer número entero: "))
num_b = int(input("Introduce el segundo número entero: "))
resultado_float = float(num_a + num_b)
print("La suma como float es:", resultado_float)

# 2. Pide al usuario un número decimal y conviértelo a string. Muestra el tipo antes y después.
num_decimal = float(input("Introduce un número decimal: "))
print("Tipo antes de convertir:", type(num_decimal))
num_str = str(num_decimal)
print("Tipo después de convertir:", type(num_str))

# 3. Convierte el string "1234" a entero y súmale 10. Muestra el resultado.
cadena = "1234"
entero = int(cadena)
print("1234 + 10 =", entero + 10)

# 4. Dado el booleano True, conviértelo a entero y a string. Muestra ambos resultados.
valor_bool = True
print("True como entero:", int(valor_bool))
print("True como string:", str(valor_bool))

# 5. Pide al usuario un número y muestra si es par o impar usando conversión a int.
num_usuario = int(float(input("Introduce un número para saber si es par o impar: ")))
if num_usuario % 2 == 0:
    print("Es par")
else:
    print("Es impar")