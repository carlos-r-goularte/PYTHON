nome = ['Carlos','Carolina','Pedro','Rodrigo','Eduardo','Nicolas','Miguel']

def opcao():
    opcao = input('''Digite uma opção: 
    1 - Imprimir Dados
    2 - Inserir Dados
    3 - Buscar Dados
    X - Sair
    
    :''')
    print("")
    if opcao == '1':
        imprimir()
    elif opcao == '2':
        inserir()
    elif opcao == '3':
        buscar()
    elif opcao.upper() == 'X':
        exit() 
    else:
        print("Opção inválida, tente novamente!")

def imprimir():
    opcao_imprimir = input("Digite o numero do índice que você quer imprimir, ou escreva 'todos' para imprimir todos os elementos: ")
    print("")

    try:
        if opcao_imprimir.upper() == 'TODOS':
            for indice in range(0,len(nome)):
                print(f"Nome.{indice + 1}: {nome[indice]}")
        else:
            print(f"Nome.{int(opcao_imprimir)}: {nome[int(opcao_imprimir) - 1]}")
    except:
        print("Ocorreu um erro, tente novamente!")
        opcao()

def inserir():
    indice = input("Digite a posição em que você quer inserir o valor [escreva 'ultima' para inserir no final da lista]: ")
    valor = input("Digite o valor que você quer inserir: ")
    try:
        if indice.upper() == 'ULTIMA':
            nome.append(valor)
        else:
            nome.insert(int(indice) - 1,valor)
    except:
        print("Erro, tente novamente!")

def buscar():
    busca = input("Digite o nome do elemento que você deseja buscar ou a posição do mesmo: ")

    try:
        if not busca.isdigit():
            for indice in range(0,len(nome)):
                if busca == nome[indice]:
                    print(f"Nome.{indice + 1}: {nome[indice]}")
                    elemento_busca = indice
        elif busca.isdigit():
            print(nome[int(busca)-1])
            elemento_busca = int(busca)-1
        
        menu(elemento_busca)
        
    except:
        print("Elemento não encontrado!")
        
def excluir(elemento):
    del[nome[elemento]]
    print("Elemento excluido com sucesso!")

def alterar(elemento):
    nome[elemento] = input("Digite o novo valor do elemento: ")
    print("Elemento alterado com sucesso!")

def menu(x):
    menu = input('''Digite uma opção: 
    1 - Alterar Elemento
    2 - Excluir Elemento
    X - Voltar para o menu
    :''')
    print("")
    if menu == '1':
        alterar(x)
    elif menu == '2':
        excluir(x)
    elif menu.upper() == 'X':
        opcao() 
    else:
        print("Opção inválida, tente novamente!")

while True:
    print("")
    opcao()
    print("")
