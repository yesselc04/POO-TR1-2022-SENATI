from Trabajador import Trabajador

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

alu= Trabajador(nom , cat, he,tar)
  
print("NOMBRE:                     ",alu.Nombre())
print("CATEGORIA:                  ",alu.Categoria())
print("SUELDO BÁSICO:               S/.",alu.Sueldo_basico()) 
print("DESCUENTO TARDANZA:          S/.",alu.Descuento())
print("PAGO HORAS EXTRAS:           S/.",alu.Horas_extras())
print("SUELDO NETO:                 S/.",alu.Sueldo_neto())
print("")