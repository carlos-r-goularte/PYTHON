from string import Template

def main():
    # utilização do metodo format()
    frase = "Curso: {0} || Aluno: {1}".format("Python Avançado","Carlos Rodrigo Goularte")
    print(frase)

    #utilizando placeholders e metodo substitute
    templ = Template("Curso: ${curso} || Aluno: ${nome}")
    frase_2 = templ.substitute(curso = "Python Avançado", 
    nome = "Carlos Rodrigo Goularte")
    print(frase_2)

    #usar o metodo substitute com um dicionário
    dados = {"curso": "Python Avançado", 
    "nome": "Carlos Rodrigo Goularte"}
    frase_3 = templ.substitute(dados)
    print (frase_3)

if __name__ == "__main__":
    main()

