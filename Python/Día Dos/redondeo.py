#Redondeo

#El redondeo facilita la interpretación de los valores calculados al limitar la cantidad de decimales y presentar un resultado más claro y conciso.

#En Python, la función round() se utiliza para redondear números. Esta función puede tomar uno o dos argumentos:
# - El número que se desea redondear.
# - (Opcional) La cantidad de decimales a los que se desea redondear.

print(round(3.14159, 2))
print(round(2.71828))

numero = round(2.71828,3)
print(numero)


# Ejercicios:
# 1. Redondea el número 9.87654321 a 4 decimales y muestra el resultado.
print(round(9.87654321, 4))

# 2. Redondea el número 15.499 a 0 decimales y muestra el resultado.
print(round(15.499))

# 3. Pide al usuario un número decimal y redondéalo a 1 decimal.
num_usuario = float(input("Introduce un número decimal: "))
print(round(num_usuario, 1))

# 4. Redondea el resultado de la división 22/7 a 3 decimales y muestra el resultado.
print(round(22/7, 3))