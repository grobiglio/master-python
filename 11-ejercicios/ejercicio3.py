"""
Ejercicio 3:
Programa que compruebe si una variable está vacía, y si lo está rellenarlo con texto en
minuscula y mostrarlo en mayúscula
"""
# Variable
variable = ""

# if variable=="":
if len(variable.strip())==0: # Considera la variable vacía aunque tenga espacios
    texto = input ("Ingresar texto para rellenar variable: ")
    variable = texto.lower()
    print (f"La variable ahora tiene: {variable}")
    print (f"Pero te muyestro: {variable.upper()}")
else:
    print (f"La variable tiene el valor: {variable}")