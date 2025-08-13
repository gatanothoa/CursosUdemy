#La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones

nombre = input("¡Hola! ¿Cuál es tu nombre?: ")
ventas = float(input("Por favor dime cuanto vendiste: "))
comision = round(ventas * 0.13, 2)

print (f"¡Hola {nombre}. Veo que vendiste ${ventas} pesos.")
print(f"¡Felicidades {nombre}!")
print(f" Ahora tu comisión por tus ventas es de ${comision} pesos!")
print("¡Sigue trabajando duro!")
