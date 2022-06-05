# Importar módulo SQLite
import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer Producto 1', 'Descripción del producto', 550)")
conexion.commit()
"""

# Borrar registros
"""
cursor.execute ("DELETE FROM productos")
conexion.commit()
"""

# Insertar muchos registros de golpe
productos = [
    ('Tele', 'Buen tele', 500),
    ('Compu', 'Buena compu', 100)
]
cursor.executemany("INSERT INTO productos VALUES (NULL, ?, ?, ?)", productos)
conexion.commit()

# Listar datos
cursor.execute ("SELECT * FROM productos;")
productos = cursor.fetchall()
print (productos)

# Cerrar conexión
conexion.close()