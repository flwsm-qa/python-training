#Diccionarios, como las listas pero el indice es una key

dicc = {"nombre": "Mica", "Edad": 25, "verdad": True}
#print(dicc.get("apellido", "Key no valida"))

dicc["verdad"] = False #cambiar algo en el diccionario

print(dicc)

# for key, value in dicc.items(): #print de las keys del diccionario .item devuelve tambien los valores ademas de als keys
#     print(value)
#     print (key)

# id "edad" in dicc:
# print("Hay edad")

#Agregar elementos

dicc["Color"] = "Azul"
print(dicc)
