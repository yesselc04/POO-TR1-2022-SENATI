class Estudiante: # creamos la clase padre

    def __init__(self, edad,nombre): #definimos  los parametros edad y nombre

      self.edad = edad # declaramos el atributo edad es igual al argumento edad
      self.nombre = nombre # declaramos el atributo nombre es igual al argumento nombre


class IngenieriaSoftware(Estudiante): # en el parenteses indicamos la clase padre o clase principal Estudiante

    def presentarse(self): # creamos el metodo presentarse
        print("Hola soy ", self.nombre, 'tengo', self.edad, "años y estudio Inteligencia artificial en Ingenieria de Software")

Jhon = IngenieriaSoftware(30 ,"Jhon Doe")

Jhon.presentarse()
