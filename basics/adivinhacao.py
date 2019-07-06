print("****************************************")
print("Seja bem-vindo ao jogo de adivinhação")
print("****************************************")

numero_secreto = 42

chute_str = input("Digite o número:")
print("Você digitou: ", chute_str)
chute = int(chute_str)


if(chute == numero_secreto):
    print("Parabens! você acertou!")
else:
    if(chute < numero_secreto ):
        print("O seu chute foi menor que o número secreto.")
    elif(chute > numero_secreto ):
        print("O seu chute foi maior que o número secreto.")

print("Fim de jogo")