"""
Ejercicio 4:
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano
y que imprima un mensaje según el tipo de dato de cada variable. Usar funciones.
"""

def tipoDatos (variable):
    if isinstance(variable, list):
        mensaje = f"La variable {variable} es una LISTA"
    elif isinstance(variable, str):
        mensaje = f"La variable {variable} es una CADENA"
    elif isinstance(variable, int):
        if str(variable)=='True' or str(variable)=='False':
            mensaje = f"La variable {variable} es BOOLEANA"
        else:
            mensaje = f"La variable {variable} es un ENTERO"
    else:
        mensaje = f"No sé de que tipo es la variable {variable}."
        
    return mensaje

# Defino mis 4 variables
lista = [1, 2]
cadena = 'String'
entero = 1
booleana = False

print (tipoDatos(lista))
print (tipoDatos(cadena))
print (tipoDatos(entero))
print (tipoDatos(booleana))