def minha_funcao(arg1,arg2, *, suprimir_exceptions=False):
    print(arg1,arg2,suprimir_exceptions)


def main():
    minha_funcao(1,2,suprimir_exceptions=True)


if __name__ == "__main__":
    main()