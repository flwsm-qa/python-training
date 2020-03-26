#Tuplas. Como las listas pero no se pueden modificar
#Loop. Se repite hasta que se cumple una condicion. While, For. 
import random
numeros = [6,5,3,8,2,5,4,11]

# for num in numeros: #para cada numero adentro de la variable numeros se va a repetir el codigo siguiente
#     print(num)

# for i in range(10): #para cada valor del rango 10 hace print
#     print(i)
 
 #PREGUNTAR ^

#List Comprehension

# tabla2 = [(i+1)*2 for i in range(10)]
# print(tabla2)


alumnos = [] #lista vacia

for i in range(30):
    notas = [random.randint(1,10) for i in range (3)]
    alumnos.append(notas)
print(alumnos)

promedios =[]
for i in range (30):
    notas = alumnos[i]
    suma = 0
    for nota in notas:
        suma = nota + suma
    promedios.append(suma/3)

print(promedios)