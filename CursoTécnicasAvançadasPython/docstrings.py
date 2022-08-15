def minha_funcao(arg1, arg2=None):
    '''Minha função que faz um print dos argumentos passados
    
    Params:
        arg1: primeiro argumento, algo interessante.
        arg2: segundo argumento, Default: None.
        
    '''
    print(arg1,arg2)


def main():
    print(minha_funcao.__doc__)


if __name__ == "__main__":
    main()