"""
Módulos: funcionalidades ya hechas para reutilizar

Puedo consultar los módulos de Python aquí:
https://docs.python.org/3/py-modindex.html#cap-m

Los módulos vienen en el lenguaje, los puedo conseguir en interner
o puedo crear mis proipios módulos.
"""
"""
# Importar módulo
import mimodulo

print (mimodulo.holaMundo("Guillermo"))
print (mimodulo.calculadora(23,4))
"""
"""
# Importar solamente una función del módulo
from mimodulo import holaMundo

print (holaMundo("Guillermo"))
"""
"""
# Importar todas las funciones de un módulo para no tener que llamarlas como
# métodos del módulo sino directamente con el nombre de la función
from mimodulo import *

print (holaMundo("Guillermo"))
print (calculadora(23,4))
"""
"""
# Módulo de fechas
import datetime

print (datetime.date.today())
fecha_completa = datetime.datetime.now()
print (fecha_completa)
anio = fecha_completa.year
print (anio)
print (fecha_completa.day)
print (fecha_completa.weekday())

fecha_pers = fecha_completa.strftime("%d/%m/%Y")
print ("Fecha personalizada:",fecha_pers)
"""
# Módulo matemáticas
import math
print ("La raíz cuadarada de 10 es", math.sqrt(10))
print ("El número pi es", math.pi)