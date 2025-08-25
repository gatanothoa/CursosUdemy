#Son las estructuras de datos que almacenan múltiples elementos en una sola variable.
#A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.
#Ocupan menos espacio en memoria que las listas.

tupla = (1, 2, (10,20), 4, 5)
tupla = list(tupla)
print(tupla)

t = (1,2,3,1,1,1,1,1,1)

print(t.count(1))
print(t.index(3))

mi_tupla = (1, 2, 3, 4, 5)

a,b,c,d,e = mi_tupla

print(a)
print(b)
print(c)
print(d)
print(e)
