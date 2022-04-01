class Promedio:
    def __init__(self,n1,n2):
        self.nota1=n1
        self.nota2= n2
        
    def Calcular(self):
        return((self.nota1 + self.nota2) /2)
    
class PromedioPeso(Promedio):
     #n1 -----> peso 1
     #n2------>peso3
     #act----->peso 1
     
     def __init__(self,n1,n2,act):
         
         Promedio.__init__(self,n1,n2)
         
         self.actitudinal = act
      
     def Calcular(self):
         return((self.nota1+self.nota2 +3 + self.actitudinal)/5)   
        
prom1 = Promedio(12,17)
    
print ("\nCOLEGIO JOSE GALVEZ") 
print("="*19)
print ("\nCONSULTAS DE NOTAS") 
print("="*17)
print("Curso.......: Historia")
print("Nota 1.........:", prom1.nota1)
print("Nota 2.........:", prom1.nota2)
print("Promedio.....:" , prom1.Calcular())  

prom2 =PromedioPeso(8,10,9)
print("\nCurso.......: Geografia")
print("Nota 1.........:", prom2.nota1)
print("Nota 2.........:", prom2.nota2)
print("Actitudinal....:" , prom2.actitudinal)
print("Promedio.....:" , prom2.Calcular())