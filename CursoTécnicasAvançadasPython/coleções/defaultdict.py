import collections

def main():

    #definindo uma lista de itens para contar
    frutas = ['maçâ', 'pêra', 'laranja', 'banana',
              'maçâ', 'uva', 'banana', 'banana']

    #Usando um dicionário default para contar cada elemento
    contador_frutas = collections.defaultdict(int)

    #contando elementos da lista
    for fruta in frutas:
        contador_frutas[fruta] += 1

    #print do resultado
    for (c, v) in contador_frutas.items():
        print(c + ": " + str(v))


if __name__ == "__main__":
    main()