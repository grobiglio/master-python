nada = None
cadena = "Hola, soy Guillermo Robiglio"
entero = 99
flotante = 4.2
booleano = True
lista = [10, 20, 30, 50, 100]
listaStr = [40, "Guillermo", "edad", 10]
tupla = ("Master", "en", "Python") # La tupla, a diferencia de la lista, no cambia
diccionario = {
    "nombre": "Guillermo",
    "apellido": "Robiglio",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"
# Otros tipos de datos son: set, frozen set, byte array, memory view

# Imprimir variable
print (nada)
print (cadena)
print (entero)
print (flotante)
print (booleano)
print (lista)
print (listaStr)
print (tupla)
print (diccionario)
print (rango)
print (dato_byte)

# Mostrar tipo de datos
print (type(nada))
print (type(cadena))
print (type(entero))
print (type(flotante))
print (type(booleano))
print (type(lista))
print (type(listaStr))
print (type(tupla))
print (type(diccionario))
print (type(rango))
print (type(dato_byte))

# Convertir datos
texto = "Hola, soy un texto"
numerito = str(776) # Convierte número a cadena

print (texto + " " + numerito)
print (type(numerito))

numerito = float(776) # Convierte a número decimal (de punto flotante)
print (type(numerito))
print (numerito)