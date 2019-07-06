print("****************************************")
print("Seja bem-vindo ao jogo de adivinhação")
print("****************************************")

numero_secreto = 42
rodada = 1
total_tentativas = 3

while (rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite o número:")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabens! você acertou!")
    else:
        if(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        elif(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
    rodada = rodada + 1

print("Fim de jogo")