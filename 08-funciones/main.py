"""
Ejemplo 1
print ("---- Ejemplo 1 ----")

# Definir función
def muestraNombre ():
    print ("Guillermo")
    print ("Ariel")
    print ("\n")

# Invocar función
muestraNombre()
"""
"""
Ejemplo 2: parámetros
print ("---- Ejemplo 2 ----")

def mostrarTuNombre(nombre, edad):
    print (f"Tu nombre es {nombre}")
    if edad>18: print ("Y eres mayor de edad")

nombre = "Guillermo"

while nombre != "":
    nombre = input ("Introduce tu nombre: ")
    edad = int(input ("Introduce tu edad: "))
    mostrarTuNombre(nombre, edad)
"""
"""
Ejemplo 3
print ("---- Ejemplo 3 ----")
def tabla(numero):
    print (f"Tabla del {numero}")
    for contador in range (11):
        if numero>10:
            print ("Solo hasta la tabla del 10")
            break # Con esto ni siquiera se ejecuta el else 
        if contador == 0:
            continue
        print(f"{numero} x {contador} = {numero*contador}")
    else: print ("--- Tabla finalizada ---")

# numero = int(input ("¿De qué número quieres la tabla?: "))
tabla(int(input ("¿De qué número quieres la tabla?: ")))
"""
"""
Ejemplo 4: parámetros opcionales
print ("---- Ejemplo 4 ----")

def getEmpleado (nombre, dni = None):
    print ("Empleado:")
    print (f"Nombre: {nombre}")
    print (f"DNI: {dni}")

getEmpleado("Guillermo",23555828)
"""
"""
Ejemplo #5: Parámetros opcionales y devolución de datos
print ("---- Ejemplo #5 ----")

def saludame(nombre):
    saludo = f"Hola {nombre}, ¿cómo estás?"
    return saludo

hola = saludame("Guillermo")
print (hola)
"""
"""
Ejemplo #6
print ("---- Ejemplo #6 ----")

def calculadora (numero1,numero2,basicas=False):
    suma  = numero1+numero2
    resta = numero2-numero2
    mult  = numero1*numero2
    div   = numero1/numero2

    cadena = ""
    if basicas:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
    else:
        cadena += "Multiplicación: " + str(mult)
        cadena += "\n"
        cadena += "División: " + str(div)

    return cadena

print (calculadora(5,5,True))
"""
"""
Ejemplo #7: funciones dentro de funciones
print ("---- Ejemplo #7 ----")

def getNombre (nombre):
    texto = f"Nombre: {nombre}"
    return texto

def getApellido (apellido):
    texto = f"Apellido: {apellido}"
    return texto

def getTodo (nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print (getTodo("Guillermo","Robiglio"))
"""
# Ejemplo #8: Funciones lambda o funciones anónimas
print ("---- Ejemplo #8 ----")

dime_el_year = lambda year: f"El año es {year}"

print (dime_el_year(2020))