import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)


# if (dado1 < dado2 and dado1 < dado3 and dado1 < dado4):
#     suma = dado2 + dado3 + dado4

# if (dado2 < dado1 and dado1 < dado3 and dado1 < dado4):
#     suma = dado1 + dado3 + dado4

# if (dado3 < dado1 and dado1 < dado2 and dado1 < dado4):
#     suma = dado1 + dado2 + dado4

# if (dado4 < dado1 and dado1 < dado1 and dado1 < dado2):
#     suma = dado1 + dado2 + dado3

# print(f"dado1 {dado1} dado2 {dado2} dado3 {dado3} dado4 {dado4}")
# print(suma)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Fuerza %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Destreza %i"% res)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Constitución %i"% res)


dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Inteligencia %i"% res)


dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Sabiduria %i"% res)


dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)

suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1,dado2,dado3,dado4)

res = suma - menor

print("Carisma %i"% res)