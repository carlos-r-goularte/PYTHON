def primeiro_filtro(num):
    if num % 2 == 0:
        return False
    return True

def segundo_filtro(letra):
    if letra.isupper():
        return False
    return True

def quadrado(x):
    return x ** 2

def nota_para_conceito(x):
    if x >= 90:
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

numeros = (1,2,3,4,5,6,7,8,9,
        10,11,12,13,14,15,16,17,18,19,
        20,21,22,23,24,25,26,27,28,29,
        30,31,32,33,34,35,36,37,38,39,
        40,41,42,43,44,45,46,47,48,49,
        50,51,52,53,54,55,56,57,58,59,
        60,61,62,63,64,65,66,67,68,69,
        70,71,72,73,74,75,76,77,78,79,
        80,81,82,83,84,85,86,87,88,89,
        90,91,92,93,94,95,96,97,98,99,100)
num = (1,8,4,5,13,26,381,410,58,47)
letras="abcDeFGHiJklmnoP"
notas = (81,89,94,78,61,66,99,74)

#função filter:
impares = list(filter(primeiro_filtro,numeros))
print(impares,end='\n\n')
impares = list(filter(primeiro_filtro,num))
print(impares,end='\n\n')


minusculas = list(filter(segundo_filtro,letras))
print(minusculas,end='\n\n')


#função map:
quadrados = list(map(quadrado,num))
print(quadrados,end='\n\n')

#função sorted e map
notas = sorted(notas)
conceitos = list(map(nota_para_conceito,notas))
print(notas)
print(conceitos)