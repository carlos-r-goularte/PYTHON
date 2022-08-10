char = input("Digite uma letra: ").lower()

vowels = ['a','e','i','o','u']

if char in vowels:
    print("Letra digitada é uma vogal")
else:
    print("Letra Digitada é consoante")