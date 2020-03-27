#Escribir un algoritmo que, dada una lista de números ordenados 
# y un número N, te devuelva true si alguna combinación de 
# dos números cualesquiera suman N, y devuelva false si 
# ninguna combinación de dos números sumados da como resultado 
# el número N.


lista = [1,2,3,4,5,6,7,8,9]
n = 15
index = 0
valor = lista[index]

"""
for i in lista:
    if 
    suma = valor + i
    print(suma)
"""
for i in lista:
    suma = valor + lista[0]
    if suma == n:
        print("True")
    else:
        index = index+1


#A TEMRINAR
            

        
    

 