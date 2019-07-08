import random


def jogar():
    print("****************************************")
    print("Seja bem-vindo ao jogo de adivinhação")
    print("****************************************")

    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Selecione o nivel de dificuldade:")
    print("(1) Fácil - (2) Médio - (3) Difícil")
    nivel = int(input("Defina o nivel:"))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print("Nível de dificuldade invalido,")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!  \n")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            print("Sua pontuacao foi de {}".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.\n")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.\n")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()