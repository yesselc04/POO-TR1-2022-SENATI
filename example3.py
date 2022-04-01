# Escribge un programaen python para crear clases de cuenta bancaria con atributos 
# de instancia, numero de cuenta, nombre del titular, balance

class Vehicle:
    def __init__(self, numero_cuenta, nombre, balance):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.balance = balance

atributo = Vehicle(123456789, "Yessenia", 235.50)
print("El numero de cuenta es: ", atributo.numero_cuenta)
print("El nombre del titular es: : ", atributo.nombre)
print("El balance total es de: ", atributo.balance)