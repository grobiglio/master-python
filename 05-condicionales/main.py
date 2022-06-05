# Un condicional es una estructura de control
# que me permite controlar el flujo del programa
"""
Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SINO:
    Se ejecuta otro grupo de instrucciones
------------
Operadores de comparación
== igual que
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

Operadores lógicos
and
or
! (negación)
not
"""

"""
# Ejemplo 1
print ("---- Ejemplo 1 ----")
# color = "rojo"
# color = "verde"
color = input ("¿Color favorito?: ")

if color == "rojo":
    print ("El color es ROJO")
else:
    print ("El color NO es ROJO")
"""
"""
# Ejemplo 2
print ("---- Ejemplo 2 ----")

year = int(input ("¿En qué año estamos?: "))

if year >= 2021:
    print ("Estamos de 2021 en adelante.")
else:
    print ("Es un año anterior al 2021")
"""
"""
# Ejemplo 3
print ("---- Ejemplo 3 ----")

nombre = "Guillermo"
ciudad = "Barcelona"
continente = "América"
edad = 20
mayoria_edad = 18

if edad>=mayoria_edad:
    print (f"{nombre} es mayor de edad.")
    if continente!="Europa":
        print ("No es europeo")
    else:
        print (f"Es europeo y de {ciudad}")
else:
    print (f"{nombre} NO es mayor de edad.")
"""
"""
# Ejemplo 4
print ("---- Ejemplo 4 ----")

dia = int(input("Introduce el número del día de la semana: "))

if dia==1:
    print ("El día es lunes")
elif dia==2:
    print ("El día es martes")
elif dia==3:
    print ("El día es miércoles")
elif dia==4:
    print ("El día es jueves")
elif dia==5:
    print ("El día es viernes")
else:
    print ("Es fin de semana")
"""
"""
# Ejemplo 5
print ("---- Ejemplo 5 ----")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Introduce tu edad: "))

if edad_oficial >= edad_minima and edad_oficial<=edad_maxima:
    print ("Está en edad de trabajar.")
else:
    print ("No está en edad de trabajar.")
"""
"""
# Ejemplo 6
print ("---- Ejemplo 6 ----")

pais = input ("Ingrese un país: ")

if pais == "España" or pais == "Argentina" or pais == "México":
    print (f"{pais} es un país de habla hispana.")
else:
    print (f"{pais} NO es un país de habla hispana")
"""
"""
# Ejemplo 7
print ("---- Ejemplo 7 ----")

pais = input ("Ingrese un país: ")

if not (pais == "España" or pais == "Argentina" or pais == "México"):
    print (f"{pais} NO es un país de habla hispana.")
else:
    print (f"{pais} es un país de habla hispana")
"""
# Ejemplo 8
print ("---- Ejemplo 8 ----")

pais = input ("Ingrese un país: ")

if pais != "España" and pais != "Argentina" and pais != "México":
    print (f"{pais} NO es un país de habla hispana.")
else:
    print (f"{pais} es un país de habla hispana")