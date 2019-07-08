import forca
import adivinhacao
import sys

def escolhe_jogo():

    print("***********************")
    print("Escolha o jogo: ")
    print("(1) - Forca | (2) - Adivinhação | (0) - Finalizar")
    escolha = int(input("Qual o jogo? \n"))
    print("***********************")
    if (escolha == 1):
        forca.jogar()
    elif (escolha == 2):
        adivinhacao.jogar()
    elif (escolha == 0):
        print("Finalizando...")
        sys.exit()
    else:
        print("Jogo invalido ou inexistente")

    while (escolha != 1 and escolha != 2 and escolha != 0):
        print("***********************")
        print("Escolha uma das opções: ")
        print("(1) - Forca | (2) - Adivinhação | (0) - Finalizar")
        escolha = int(input("Qual o jogo? \n"))
        print("***********************")
        if (escolha == 1):
            forca.jogar()
        elif (escolha == 2):
            adivinhacao.jogar()
        elif (escolha == 0):
            sys.exit()
        else:
            print("Jogo invalido ou inexistente")

if(__name__ == "__main__"):
    escolhe_jogo()