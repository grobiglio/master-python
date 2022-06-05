# Los diccionarios tienen índices alfanuméricos en lugar de índices numéricos
"""
persona = {
    "nombre": "Guillermo",
    "apellido": "Robiglio",
    "web": "inggar.com.ar"
}
print (persona)
print (persona["apellido"])
"""
# Lista con diccionarios
contactos = [
    {
        'nombre': 'Juan',
        'email': 'juan@juan.com'
    },
    {
        'nombre': 'José',
        'email': 'jose@jose.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    }
]
# print (contactos)
# print (contactos[1]['nombre'])
print ("Lista de contactos")
print ("------------------")

for contacto in contactos:
    print (f"Nombre: {contacto['nombre']}")
    print (f"e-mail: {contacto['email']}")
    print ("----------------")
