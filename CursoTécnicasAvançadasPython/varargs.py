def adicao(*args):
    return sum(args)

def main():
    print(adicao(5,10,20))
    print(adicao(1,2,2,2,4))

    #passagem de lista como parametro
    valores = [5,10,15,20]
    print(adicao(*valores))


if __name__ == "__main__":
    main()

