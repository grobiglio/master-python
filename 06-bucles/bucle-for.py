"""
for variable in elemento_iterable (lista, rango, etc.)
    Instrucciones
"""
"""
contador = 0
resultado = 0

for contador in range(0,5):
    print ("Voy por el " + str(contador))
    resultado += contador # Esto es lo mismo que: resultado = resultado + contador

print (f"El resultado es {resultado}")
"""
"""
# Ejemplo tablas de multiblicar
print ("\n----- EJEMPLO -----")

numero_usuario = int(input ("¿De qué número quieres la tabla?: "))

if numero_usuario<1:
    numero_usuario=1

print (f"Tabla de multiplicar del número {numero_usuario}")

for numero_tabla in range (1,11):
    if numero_usuario>10:
        print ("Solo hasta la tabla del 10")
        break # Con esto ni siquiera se ejecuta el else 
        continue # Con esto salta a la próxima iteración y finalmente se ejecuta el else
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print ("--- Tabla finalizada ---")
"""
# Ejemplo tablas de multiblicar
print ("\n----- EJEMPLO -----")

numero_usuario = int(input ("¿De qué número quieres la tabla?: "))

if numero_usuario<1:
    numero_usuario=1

print (f"Tabla de multiplicar del número {numero_usuario}")

for numero_tabla in range (11):
    if numero_usuario>10:
        print ("Solo hasta la tabla del 10")
        break # Con esto ni siquiera se ejecuta el else 
    if numero_tabla == 0:
        continue # Con esto salta a la próxima iteración y finalmente se ejecuta el else
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print ("--- Tabla finalizada ---")