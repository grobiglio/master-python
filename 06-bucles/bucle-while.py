"""
contador = 1
muestrame = ""

while contador <= 100:
    print (f" Estoy en el número {contador}")
    if contador == 1:
        muestrame = str(contador)
    else:
        muestrame = muestrame + ", " + str(contador)
    contador +=1

print (muestrame)
"""

# Ejemplo tablas de multiplicar
print ("---- EJEMPLO ----")
numero_usuario = int(input ("¿De qué número quieres la tabla?: "))

if numero_usuario < 1: numero_usuario = 1

print (f"---- Tabla del {numero_usuario} ----")

contador = 1
while contador <= 10:
    print (f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print ("Fin de la tabla")