#Funciones

def my_fun(nombre):
    print(f"Soy {nombre}")


# my_fun("Mica")

def suma(a,b):
    res = a + b
    return "soy una suma", res

tipo, resultado = suma(3,4)
# print(tipo)
# print(resultado)

#RPG
import random

def get_stats():
    dados = [random.randint(1,6) for i in range(4)]
    dados.sort()
    max_dados = dados [1:]
    return sum(max_dados)

stats = {
    "Str": get_stats(),
    "Dex": get_stats(),
    "Int": get_stats(),
    "Wis": get_stats(),
    "Cons": get_stats(),
}
   
print(stats)

