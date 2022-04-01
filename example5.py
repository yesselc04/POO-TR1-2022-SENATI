# Escribir un programa en python para crear una clase artículo  con atributos de instancia: código del artículo, cantidad, precio.

# métodos: mostrar la cantidad actual, mostrar el precio, reducir la cantidad actual, incrementa la cantidad actual

class Articulo:
    def __init__(self,codigo,cantidad,precio):
        self.codg = codigo
        self.cantd = cantidad
        self.prec = precio
    
    def cantidad_actual(self):
        print("La cantidad actual es de",self.cantd,"unidades")
        
    def mostrar_precio(self):
        print("El precio del producto es S/ ",self.prec)
        
    def vender(self,unidades_vendidas):
        if unidades_vendidas <= self.cantd:
           self.cantd -= unidades_vendidas
           #self.cantd = self.cantd - unidades_vendidas
        else:
            print("cantidad insuficiente")
    
    def comprar(self, unidades_compradas):
        if unidades_compradas > 0:
            self.cantd =self.cantd + unidades_compradas

articl1 = Articulo(111, 20, 6.9)
articulo_jabon = Articulo(222,50,12)

#articl1.mostrar_precio()
#articl1.vender(5)
#articl1.comprar(20)
#articl1.cantidad_actual()

articulo_jabon.mostrar_precio()
articulo_jabon.vender(5)
articulo_jabon.comprar(20)
articulo_jabon.cantidad_actual()
articulo_jabon.vender(80)