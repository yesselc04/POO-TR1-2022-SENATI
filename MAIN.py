
from BOLETA import BOLETA
from TRABAJADOR import TRABAJADOR

print("")
print("=="*30)
print("    La empresa FERROTEK SAC     ")
print("=="*30)
print("")
print("....................................")
print("    ** DATOS  DE  ENTRADA **    ")
print("....................................")
 
nom= input("TRABAJADOR:                 ")
 
cat = ""

while not (cat == "A" or cat== "B" or cat == "C"):
    cat = str(input("CATEGORIA [A / B / C]:      "))
    if not (cat =="A" or cat== "B" or cat == "C"):
            print("Categoria incorrecta....")    
  
 
he= float(input("HORAS EXTRAS:               "))
tar=float(input("TARDANZA(minutos):          "))
 
print("")
print("....................................")
print("    ** BOLETA  DE  PAGO  **     ")
print("....................................") 

alu1 = TRABAJADOR(nom)
alo = BOLETA(cat, he, tar)

print("NOMBRE:                     ",alu1.Nombre())
print("CATEGORIA:                  ",alo.Categoria())
print("SUELDO BÁSICO:               S/.",alo.Sueldo_basico()) 
print("DESCUENTO TARDANZA:          S/.",alo.Descuento())
print("PAGO HORAS EXTRAS:           S/.",alo.Horas_extras())
print("SUELDO NETO:                 S/.",alo.Sueldo_neto())
print("")