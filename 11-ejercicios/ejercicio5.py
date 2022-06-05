# Ejercicio 5

vid_juegos = [
    {
        'titulo': 'GTA',
        'genero': 'Acción'
    },
    {
        'titulo': 'COD',
        'genero': 'Acción'
    },
    {
        'titulo': 'PUGB',
        'genero': 'Acción'
    },
    {
        'titulo': 'ASSINS',
        'genero': 'Aventura'
    },
    {
        'titulo': 'CRASH',
        'genero': 'Aventura'
    },
    {
        'titulo': 'PRINCE',
        'genero': 'Aventura'
    },
    {
        'titulo': 'FIFA',
        'genero': 'Deportes'
    },
    {
        'titulo': 'PRO',
        'genero': 'Deportes'
    },
    {
        'titulo': 'MOTO',
        'genero': 'Deportes'
    }
]

generos = ['Acción', 'Aventura', 'Deportes']
for gen in generos:
    print (f"Lista de video juegos de {gen}:")
    for vid_juego in vid_juegos:
        if vid_juego['genero']==gen:
            print (vid_juego['titulo'])