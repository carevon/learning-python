# LIST COMPREHENSION
inteiros = [1,3,4,5,7,8,9]
frutas = ["maçã", "banana", "laranja", "melancia"]

# NUMERO AO QUADRADO
quadrados = [n*n for n in inteiros]

# NUMEROS PARES
pares = [x for x in inteiros if x % 2 == 0]

# LETRAS MAIUSCULAS
lista = [fruta.upper() for fruta in frutas]
