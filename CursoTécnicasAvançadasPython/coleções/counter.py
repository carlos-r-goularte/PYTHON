from collections import Counter
from re import A

def main():
    
    turma_a = ["Bárbara","João","Carlos","Dário","Priscila",
    "Ana","Kevin","João","Marina",
    "Bianca","Gustavo","Carlos","Carolina","Eduardo","Nicole"]

    turma_b = ["Hiro","Bruno","Claudia","Débora","Fernanda",
    "Gabriela","Leticia","João","Jairo",
    "Samuel","Taciana","Gabriel"]

    #Criação de counter para as turmas 1 e 2
    a = Counter(turma_a)
    b = Counter(turma_b)

    
    print(a["João"])
    print(b["Carlos"])


    print(sum(a.values()))
    print(sum(b.values()))

    a.update(turma_b)
    print(sum(a.values()))

    print(a.most_common())
    print(a.most_common(3))

    a.subtract(turma_b)

    print(sum(a.values()))
    print(a.most_common(3))
    
    
    print(a & b)

if __name__ == "__main__":
    main()