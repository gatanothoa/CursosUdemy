#Son otro tipo de estructuras de datos que almacenan elementos únicos y no ordenados.
#Se utilizan para realizar operaciones de conjunto, como uniones e intersecciones.
#sus elementos son inmutables, no se pueden incluir listas 

conjunto = set([4, 5, 6, 7, 8])
print(conjunto)

conjunto1 = {1, 2, 3,(1,4,2,3,5), 4, 5,5,5,5,5,5}
print(conjunto1)

print(2 in conjunto1)
print("hola" in conjunto1)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))

s1.add(9)
print(s1)

s1.remove(2)
print(s1)

sorteo = s1.pop()
print(sorteo)


