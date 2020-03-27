#Escribir un algoritmo que encuentre el máximo y el minímo número dentro de una lista de números enteros desordenados

lista = [65,4,3,88,80,2,6,100,7]

# mas_bajo = min(lista)
# print(mas_bajo)
# mas_alto = max(lista)
# print(mas_alto)


menor = lista[0]
mayor = lista[0]
for i in lista: 
    if i < menor:
        menor = i
    if i > mayor:  
        mayor = i
print(f"{menor}, {mayor}")




