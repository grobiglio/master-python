mi_texto = "Master"
mi_texto2 = "en Python"

texto_unido = mi_texto + " " + mi_texto2
print (texto_unido)

texto_unido = f"{mi_texto} {mi_texto2}"
print (texto_unido)

mi_texto2 = "en \"Python\""

texto_unido = mi_texto + " " + mi_texto2
print (texto_unido)

mi_texto2 = 'en "Python"'

texto_unido = mi_texto + " " + mi_texto2
print (texto_unido)

texto_unido = mi_texto + "\n" + mi_texto2 # El \n introduce un salto de línea
print (texto_unido)

texto_unido = mi_texto + "\t" + mi_texto2 # El \t introduce una tabulación
print (texto_unido)

texto_unido = mi_texto + "\r" + mi_texto2 # El \r borra todo lo que hay antes
print (texto_unido)