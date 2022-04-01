#herencia unica: permite que una clase derivada herede caracterisitcas de una sola clase principal

class Empleado(): #este es el la clase padre
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

class EmpleadoSupervisor(Empleado): #Este es la clase hija
    def __init__(self, nombre, edad, salario, id):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.id = id

empleado1 = Empleado('Raul Sanchez', 22, 1000)

print(empleado1.edad, "años")