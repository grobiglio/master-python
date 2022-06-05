"""
Añadir valores a una lista mientras que la longitud sea menor a 120,
luego mostrarlo por pantalla.
Usar while y for
"""
"""
# Primero voy a hacer una lista de 110 elementos
lista = list (range(115))

# Con bucle while
while len(lista)<120:
    nuevo_valor = int(input("Ingresar valor a añadir: "))
    lista.append(nuevo_valor)
else: print (lista)

# Con bucle for
faltantes = 120 - len(lista)
for i in range(faltantes):
    nuevo_valor = int(input("Ingresar valor a añadir: "))
    lista.append(nuevo_valor)
else: print (lista)
"""
lista = []
i = 0
"""
for i in range (120):
    lista.append(i)
    print (f"Se añadió el valor {i}")
else: print (lista)
"""
while len(lista)<120:
    lista.append(i)
    print (f"Se añadió el valor {i}")
    i += 1
else: print (lista)