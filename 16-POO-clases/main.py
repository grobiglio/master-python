# Programación Orientada a Objetos (POO)

class Auto:
    # Propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    potencia = 500
    plazas = 2
    # Métodos
    def acelerar (self):
        self.velocidad += 1
    
    def frenar (self):
        self.velocidad -= 1

    def getVelocidad (self): # Es más aconsejable acceder a las propiedades por medio de métodos
        return self.velocidad

    def setColor (self, color):
        self.color = color

    def getColor (self):
        return self.color

# Fin definición de clase

# Crear objeto llamando a la clase
auto = Auto()
print (auto.marca)

print ("Velocidad actual:",auto.getVelocidad())
auto.acelerar()
print ("Velocidad resultante:",auto.getVelocidad())

print ("Color:", auto.getColor())
auto.setColor('Amarillo')
print ("Color:", auto.getColor())

# Crear múltiples objetos
auto2 = Auto() # Este es independiente del creado anteriormente
print (auto2.getColor())