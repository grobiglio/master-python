from io import open
import pathlib

# Abrir archivo
# archivo = open ("14-sistema-archivos/fichero_texto.txt", "a+")
ruta = str (pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open (ruta, "a+")

# Escribir en el archivo
archivo.write("\nEsto se escribió desde Python")

# Cerrar archivo
archivo.close()

# Abrir archivo con permiso de lectura
archivo_lectura = open (ruta, "r")

# Leer contenido
contenido = archivo_lectura.read()
print (contenido)
i = 0

for elemento in contenido:
    if elemento=="\n": i += 1

print ('Cantidad de líneas:',i)