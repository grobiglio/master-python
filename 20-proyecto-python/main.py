"""
Proyecto Python y MySQL:
- Abrir asistente
- Login o Registro
- Si elegimos registro, creará un usuario en la BBDD
- Si elegimos login, identifica al usuario y nos preguntará
  - Crear notas
  - Mostrar notas
  - Borrar notas
"""
from usuarios import acciones # Es lo mismo que escribir import usuarios.acciones

print ("""
Acciones disponibles:
  - registro
  - login
""")

hazEl = acciones.Acciones()
accion = input ("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()