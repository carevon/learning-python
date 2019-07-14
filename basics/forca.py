def jogar():
    print("****************************************")
    print("Seja bem-vindo ao jogo de adivinhação")
    print("****************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):


        chute = input("Qual seu chute? ")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:

            if (chute.upper() == letra.upper()):
                print("A palavra secreta contem a letra {} na posicao {}".format(chute, index))
            index = index + 1

        print("Jogando...")

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()