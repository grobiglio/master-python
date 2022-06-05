# Es recomendable tener un objeto por archivo e importarlos cuando sea necesario

class Auto:
    # Propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    potencia = 500
    plazas = 2

    publico = "Atributo publico"
    __privado = "Atributo privado"
    
    def __init__(self, color, marca, modelo, velocidad, potencia, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.plazas = plazas
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

    def getPrivado (self):
        return self.__privado

# Fin definición de clase