class BOLETA:

    def __init__(self,cat , he, tar):
          self.horas = he
          self.tardanza = tar
          self.categoria = cat


    def Nombre (self):
        return self.nombre

    def Categoria(self):
        return self.categoria

    def Sueldo_basico (self):

        e=0


        if(self.categoria== "A"):
            e= 3000
        elif(self.categoria== "B"):
            e= 2500
        elif(self.categoria== "C"):
            e= 2000

        return e
    def Descuento(self):
       return self.Sueldo_basico()/240/60*self.tardanza
       
    def Horas_extras(self):
        return self.Sueldo_basico()/240*self.horas
      
    def Sueldo_neto(self):
        return self.Sueldo_basico()-self.Descuento()+self.Horas_extras() 
   
        

            

    