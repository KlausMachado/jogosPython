import random

def mensagem_iniciando_game():
    print("**************")
    print("jogo da forca")
    print("**************")


def selecionando_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # abrindo o arquivo txt no modo read
    palavras = []

    for linha in arquivo:  # para cada linha que tem arquivo
        linha = linha.strip()  # retirando espaços em braco e marcações da palavra
        palavras.append(linha)  # adicionar a linha na variavel palavras

    numero = random.randrange(0,
                              len(palavras))  # pegando um numero aleatorio entre 0 e a quantidade de elementos em palavras
    palavra_secreta = palavras[numero].upper()  # o indice será o número aleatório
    return palavra_secreta


def definindo_quantidade_caracter(palavra):
    return  ["_" for letra in palavra]


def chute_do_jogador():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute


def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1

def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar_forca():
    mensagem_iniciando_game()
    palavra_secreta = selecionando_palavra_secreta()
    letras_acertadas = definindo_quantidade_caracter(palavra_secreta) #coloca o _ para cada letra
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while not enforcou and not acertou:
        print('jogando...')

        chute = chute_do_jogador()

        if chute in palavra_secreta:
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7 #passamos o valor max de erros ate que enforcou seja true
        acertou = '_' not in letras_acertadas #passamos que acertou é true quando não tiver '_' em letras-acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
if __name__ == '__main__':
    jogar_forca()
