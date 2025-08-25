mi_lista = [1, "hola", 3.14, True]
mi_lista2 = [2, "adios", 6.28, False]
resultado = len(mi_lista)
resultado1 = mi_lista[0::]
mi_lista[0] = "nuevo valor"
mi_lista.append("agregado")
lista = ["g", "k","z","e"]
lista.sort()
lista.reverse()
print(lista)

print(type(mi_lista))
print(resultado)
print(resultado1)
print(mi_lista + mi_lista2)
print(lista)