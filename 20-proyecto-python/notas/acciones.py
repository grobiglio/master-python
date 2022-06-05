import notas.nota as modelo

class Acciones:

    def crear (self, usuario):
        print (f"\nOk {usuario[1]}! Vamos a Crear una nueva nota... ")
        titulo = input ("Introduce el título de tu nota: ")
        descripcion = input ("Contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print (f"\nPerfecto, has guardado la nota {nota.titulo}")
        else:
            print (f"\nNo se ha guardado la nota, lo sieto {usuario[1]}")

    def mostrar (self, usuario):
        print (f"\nVale {usuario[1]}!! Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0],"","")
        notas = nota.listar()

        for nota in notas:
            print ("\n----------------------")
            print (nota[2])
            print (nota[3])

    def borrar (self, usuario):
        print (f"\nOkey {usuario[1]}, vamos a borrar notas")

        titulo = input("Introduce el título de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print (f"Hemos borrado la nota {nota.titulo}")
        else:
            print ("No se ha borrado la nota")