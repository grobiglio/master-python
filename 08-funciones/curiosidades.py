# Se recomienda definir todas las funciones al inicio del fichero
# Lo recomendable siempre es que la función devuelva un dato

def saludo1():
    return f"Hola {nombre}, ¿cómo estás?"

def saludo2():
    return f"¿Cómo estás, {nombre}"

nombre = "Guillermo"

print (saludo1()) # Lo importante es que la variable se haya definido antes de invocar la función
print (saludo2())

# Mejor práctica sería usar argumentos en las funciones en lugar de variables globales
# Lo óptimo es que las funciones sean independientes del código general