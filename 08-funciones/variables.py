# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres."
print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print (frase)

    global iniciales
    iniciales = "GAR"

holaMundo()

print(frase)
print(iniciales)