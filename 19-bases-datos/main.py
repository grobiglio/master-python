import mysql.connector

# Conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# Verificar conexión
# print (database)

# Cursor
cursor = database.cursor(buffered=True)

"""
cursor.execute ("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute ("SHOW DATABASES")

for bd in cursor:
    print (bd)
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehilulos (
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float (10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

cursor.execute ("SHOW TABLES")

for tabla in cursor:
    print (tabla)

# Insertar un solo registro
# cursor.execute ("INSERT INTO vehilulos VALUES (null, 'Opel', 'Astra', 18500)")

# Insertar varios registros
coches = [
    ('Seat', 'Ibiza', 5000),
    ('VolkWagen', 'Polo', 10000),
    ('Citroen', 'Picasso', 8000)
]
# cursor.executemany("INSERT INTO vehilulos VALUES (null, %s, %s, %s)", coches)
database.commit()

# Listar
cursor.execute("SELECT * FROM vehilulos WHERE precio < 9000 AND marca = 'Seat'")
result = cursor.fetchall()

for coche in result:
    print (coche[1], coche[3])

cursor.execute("SELECT * FROM vehilulos")
coche = cursor.fetchone()
print (coche)

# Borrar
cursor.execute ("DELETE FROM vehilulos WHERE marca = 'Seat'")
database.commit()
print (cursor.rowcount, 'borrados!!')

# Actualizar
cursor.execute ("UPDATE vehilulos SET modelo='Xara' WHERE marca='Citroen'")
database.commit()
print (cursor.rowcount, 'actualizados!!')