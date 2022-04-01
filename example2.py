#escribe un oprograma en python para crear una clase vehicle con atributos de instancia
# max_speed milage(max velocidad y kilometraje)

class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

modelotoyota = Vehicle(240, 20)
print("La velocidad del vehiculo Toyota es: ", modelotoyota.max_speed)
print("El kilometraje recorrido por Toyota es: ", modelotoyota.milage)