class Producto:
    def __init__(self,referencia,nombre,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.descripcion = descripcion
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"
class Adorno(Producto):
    pass
adorno = Adorno(2034, "Vaso adornado", "Vaso de porcelana")
print(adorno)