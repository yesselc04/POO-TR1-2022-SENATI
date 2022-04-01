# Encapsulación:
#es el proceso de mantener los datos y metodos junto como una unidad

#Ventajas de la encapsulación:
#. las clases hacen que el codigo sea facil de cambiar y mantener
#. las propiedades que se ocultyan se puede especificar

class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def display_user(self):
        print('User Name is:   ', self.name)
        print('User age is:   ', self.__age)

user1 = User('Jhon Doe', 35)
#llamando al metodo de a clase
user1.Display_user()

#user1.name
#user1._User__age

    


class Robot:
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123

yorobot = Robot()

print(yorobot.a)
print(yorobot._b)
print(yorobot._Robot__c)
