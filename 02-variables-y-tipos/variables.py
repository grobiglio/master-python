"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""

# Crear variables y asignarles un valor
# No es necesario declarar variables en Python
texto = "Master en Python"
# texto = 1 # Esto puede ser porque Python es un lenguaje debilmente equipado
texto2 = "Guillermo Robiglio"
numero = 45
decimal = 6.7

# Mostrar valor de las variables
print (texto)
print (texto2)
print (numero)
print (decimal)

print ("-------------------")

# Sustituir el valor de algunas variables reasignando valores
numero = 77
decimal = 8.9
print (numero)
print (decimal)

print ("-------------------")

# Concatenación
nombre = "Guillermo"
apellido = "Robiglio"
iniciales = "GAR"

print (nombre + " " + apellido + " - " + iniciales)
print (f"{nombre} {apellido} - {iniciales}") # Esta es la forma que más le gusta al instructor
print ("Hola, me llamo {} {}; mis iniciales son: {}".format(nombre, apellido, iniciales))

print (nombre, apellido, iniciales) # Esto no es una concatenación