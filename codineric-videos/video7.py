nota = int(input("Ingresar nota: "))

prom = 0
cant = 0

while(nota !=0):
    if(nota >= 0 and nota <= 10):
        prom = nota + prom
        cant = cant + 1
        nota = int(input("Ingresar nota: "))
    else: 
        nota = int(input("Valor fuera de rango. Ingrese Nota entre 1 y 10. 0 para salir "))

print("Total para Promedio %.2f y Cantidad de Notas: %i"% (prom,cant))
prom_final = prom/cant
print("promedio final %.2f"% prom_final)

