# LEARNING HOW TO WRITE AND READ FILES

# ESCREVENDO EM UM ARQUIVO
arquivo = open("palavras.txt", "w", encoding="UTF-8")
frutas = {"Morango\n", "Melancia\n", "Banana\n", "Maça\n", "Abacate\n"}
for fruta in frutas:
    arquivo.write(fruta)

# LER A PRIMEIRA LINHA
# Romário 37
# Junior 32
# Daniel 28
# Izzy 38

arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)

# LER TO;DO O ARQUIVO
# Banana
# Maçã
# Pera
# Uva
# Jamelão

arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)
