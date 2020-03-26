'''
print(5 < 10) #True
print(2 > 20) #False
print(6 <= 6) #True
print(0 == 0) #True
'''

uno = int(input("Primer nota: "))
dos = int(input("Segunda nota: "))
tres = int(input("Tercer nota: "))

prom = (uno + dos + tres)/3
print("El promedio es %.2f"%prom)

if (prom > 6):
    print("Aprobado")
else:
    print("Desaprobado")
