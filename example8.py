# Herencia multiple: permite que una clase derivada herede de mas de una clase base o padre 

# class  ClaseDerivada (ClaseA, Clase B)
#......."Contenido de la clase....."
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Instituto:
    def presentarinstituto(self):
        print('Estudio en SENATI')

class InteligenciaArtifical(Estudiante, Instituto): #en el parentesis presentamos loas c lases padre
    def presentarse(self):
        print("Hola soy ", self.nombre, 'tengo', self.edad, "años y estudio Inteligencia artificial en Ingenieria de Software")

estudiante1 = InteligenciaArtifical('Jhon Doe', 20)
estudiante1.presentarse()
estudiante1.presentarinstituto()
