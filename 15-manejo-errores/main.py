# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores

"""
try:
    num1 = int(input ("Ingrese un número: "))
    num2 = int(input ("ingrese otro número: "))
    sum = num1+num2
except:
    print ("¡Debe ingresar un número entero!")
else:
    print (f"La suma {num1} + {num2} es {sum}")
finally:
    print ('Fin')
"""
try:
    num_ing = input ('Ingresá un número para elevarlo al cuadrado: ')
    num = int(num_ing)
    print (f"El cuadrado de {num} es {num**2}")
except Exception as e:
    print (type(e))
    print ("Ocurrió un", type(e).__name__)
#   print ("Numero" + num
"""
except ValueError:
    print ("¡Debés ingresar un número!")
except TypeError:
    print ("¡No se puede concatenar!")
"""
