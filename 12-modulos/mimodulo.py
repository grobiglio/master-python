
def holaMundo(nombre):
    return f"Hola, ¿cómo estás, {nombre}?"

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