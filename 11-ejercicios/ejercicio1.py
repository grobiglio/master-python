"""
Lista con 8 números enteros
1. Recorrerla y mostrarla
2. Hacer una función que recorra listas de numeros y devuelva un string para mostrarla
3. Ordenarla y mostrarla
4. Mostrar su longitud
5. Buscar algún elemento dentro de la lista en base a lo que el usuario pida por teclado
"""
# Primero voy a hacer la función
def recorrerLista (lista):
    cadena = ""
    cantidad = len(lista)
    for elemento in lista:
        if cantidad>1:
            cadena += str(elemento) + ', '
        else:
            cadena += str(elemento)
        cantidad -=1
    return cadena

# Lista de 8 números enteros
lista = [4, 5, 16, 23, 1, 10, 20, 18]
print (f"1. He creado la lista {lista}")

# Voy a recorrer y mostrar la lista
print ("\n2. Voy a recorrer y mostrar la lista.")
for numero in lista:
    print (numero)

# La voy a recorrer y mostrar como string por medio de la función
print ("\n3. Voy a recorrer y mostrar la lista como string por medio de una función.")
print (recorrerLista(lista))

# La voy a ordenar y mostrar
lista.sort()
print (f"\n4. He ordenado la lista: {lista}")

# Voy a mostrar su longitud
print (f"\n5. La longitud de la lista es {len(lista)}")

# Buscar algún elemento de la lista
elemento = int(input("\n6. ¿Qué elemento buscás?: "))
print (elemento in lista)

# Busqueda en la lista
elemento = (input("\n7. ¿Qué elemento buscás?: "))

while elemento <= 0:
    elemento = int((input("\n7. ¿Qué elemento buscás?: ")))
else:
    print (f"Buscás el nro. {elemento}")

if elemento in lista:
    indice = lista.index(elemento)
    print (f"El nro. {elemento} se encuentra en la lista y corresponde al índice {indice}.")
else:
    print (f"El nro. {elemento} no se encuentra en la lista.")
