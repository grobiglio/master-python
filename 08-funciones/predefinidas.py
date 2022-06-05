nombre = "Guillermo"

# Detectar tipo de variable
comprobar = isinstance(nombre, str)
print (comprobar)

# Limpiar espacios
frase = "        mi frase        "
print (frase.strip())

# Eliminar variables
year = 2020
print (year)
del year
# print (year)

# Comprobar variable vacía
texto = ""

if len(texto)==0: print ("La variable está vacía.")
else: print (texto)

# Encontrar caracteres
texto = "La vida es bella"
print(texto.find("vida"))

# Reemplazar caracteres
nuevo_texto = texto.replace("bella","linda")
print(nuevo_texto)

# Mayúsculas y minúsculas
print (nombre)
print (nombre.upper())
print (nombre.lower())