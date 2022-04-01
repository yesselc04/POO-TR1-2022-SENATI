#crear una clase con instancia de atributos

class Employee:
    #identifica la propiedades y asignando valñores
    id_employee = 5
    salario = 2000
    departamento = "Recursos Humanos"

#crear un objeto de la clase Employee
Saul = Employee
#imprime las propiedades de Saul
print("id = ", Saul.id_employee)
print("Salario de Saul = ", Saul.salario)
print("El Área o departamento = ", Saul.departamento)
