"""
Listas (o arrays)
Son colecciones o conjuntos de datos/valores bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.
"""
"""
# Definición de listas
peliculas = ["Batman", "Spiderman", "Avengers"]
print (peliculas)

cantantes = list (["Dyango", "Pimpinela", "Sergio Denis"]) # Adentro va cualquier item iterable
print (cantantes)

years = list (range(2020,2025)) # Esto es una lista
# years = range(2020,2025) # Esto es un rango
print (years)

lista_variada = ["Texto", 10, 1.5, True]
print (lista_variada)

print (type(peliculas), type(cantantes), type(years), type(lista_variada))
"""
"""
# Índices de listas
peliculas = ["Batman", "Spiderman", "Avengers"]
print (peliculas[1]) # Comienza desde adelante, el 0 es el primero
# print (type(peliculas[1]))
print (peliculas[-1]) # Comienza desde atrás, el -1 es el último

# years = list (range(2020,2055))
# print (years[2:5])
# print (years[15:])

peliculas[1] = "Hombre araña"
print (peliculas)
"""
"""
# Añadir elementos a lista
cantantes = ["Dyango", "Pimpinela", "Sergio Denis"]
print (cantantes)

cantantes.append("Jairo")
print (cantantes)
"""
"""
# Recorrer lista

peliculas = ["Batman", "Spiderman", "Avengers"]

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input ("Introduce película: ")
    if nueva_pelicula != "parar": peliculas.append(nueva_pelicula)

print ("--------- Películas ---------")
for pelicula in peliculas:
    print (f"{peliculas.index(pelicula)+1}. {pelicula}")
"""
# Listas multidimensionales
print ("---- Listado de contactos ----")
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        'Juan',
        'juan@juan.com'
    ]
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print (f"Nombre: {elemento}")
        else:
            print (f"e-mail: {elemento}")
    print ("\n")