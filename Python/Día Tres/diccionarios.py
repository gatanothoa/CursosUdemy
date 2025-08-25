#Los diccionarios son estructuras de datos que almacenan pares de clave-valor

#Son especialmente útiles para guardar y recuperar información a partir de los nombres de sus claves.

diccionario = {
    "nombre": "Antonio",
    "edad": 40,
    "ciudad": "México",
    "datos": {
        "telefono": "123456789",
        "email": "antonio@example.com",
        "numeros": [1, 2, 3, 4, 5]
    }
}

diccionario["nueva_clave"] = "nuevo_valor"
diccionario["edad"] = 41
print(diccionario)
resultado = diccionario["nombre"]
print(resultado)
print(diccionario["datos"]["email"].upper())

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())