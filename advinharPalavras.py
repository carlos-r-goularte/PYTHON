from math import log10,ceil

def menu():
    menu = input('''\nDigite uma opção: 
    1 - Inicar Jogo
    2 - Ver Pontuação
    X - Sair do Jogo
    :''')
  
    if menu == '1':
        iniciar()
    elif menu == '2':
        placar()
    elif menu.upper() == 'X':
        exit() 
    else:
        print("Opção inválida, tente novamente!")

def iniciar():
    palavra_secreta = input("\n\nDigite a palavra secreta: ")
    dica = input("Digite uma dica: ")
    chances = limitar(palavra_secreta)
    letra_digitada = []
    secreto_temporario = '*' * len(palavra_secreta)

    while True:

        print("\n\n==============================================================================")
        print(f"Você tem [{chances}] chances para digitar letras e tentar descobrir a palavra secreta!")
        print(f"                             A dica é: {dica}")
        print(f"                                 {secreto_temporario}")
        print("==============================================================================\n\n")

        letra = input("Digite uma letra: ")

        try:
            if len(letra) > 1 or not letra.isalpha():
                print("Só é permitido digitar apenas [1] letra do alfabeto\n")
                continue
        except:
            print("Só é permitido digitar apenas [1] letra do alfabeto\n")

        
        letra_digitada.append(letra)

        if letra in palavra_secreta:
            if chances == 1:
                print("Última chance para descobrir mais uma letra: ")
                chances -= 1
            else:
                print(f"\nEba! Você acertou uma letra! Restam mais {chances - 1} tentativas\n")
                chances -= 1
        else:
            print(f"\nQue pena! Você errou a letra, mas ainda restam mais {chances - 1} tentativas\n")
            chances -= 1
            letra_digitada.pop()

        if chances == 0:
            break

        secreto_temporario = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letra_digitada:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

    print("\n\n========================================")
    print(f"Você esgotou o número de tentativas!")
    print(f"          A dica é: {dica}")
    print(f"        {secreto_temporario}")
    print("===========================================\n\n")
    palavra = input("Digite qual é a palavra secreta: ")

    print("\n---------------------------------------------------------------")
    print("Que pena! Você esgotou o número de tentativas, tente novamente!")
    print("---------------------------------------------------------------\n")
    menu()

def limitar(palavra_secreta):
    chances = ceil(log10(len(palavra_secreta))*len(palavra_secreta)/3)
    return chances

def placar():
    pass

while True:
    menu()


