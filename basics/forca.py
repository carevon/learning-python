import random

def jogar():

    imprime_msg_abertura()
    palavra_secreta =  carregar_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_ponto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor()
    print("Fim de jogo")

# MÉTODO QUE IMPRIME AS MENSAGENS DE ABERTURA
def imprime_msg_abertura():
    print("****************************************")
    print("Seja bem-vindo ao jogo de adivinhação")
    print("****************************************")

# MÉTODO QUE CARREGA AS PALAVRAS E RETORNA UMA PALAVRA ALEATÓRIA
def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# MÉTODO QUE ESCONDE CADA LETRA DA PALAVRA CARREGADA
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual seu chute? ")
    chute = chute.strip().upper()
    return chute

def marca_ponto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

def imprime_msg_vencedor():
    print("Você ganhou!!!")
def imprime_msg_perdedor():
    print("Você perdeu!!")

if(__name__ == "__main__"):
    jogar()