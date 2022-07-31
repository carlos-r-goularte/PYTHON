numInteger1= int(input("Digite um número inteiro: "))
numInteger2= int(input("Digite outro número inteiro: "))

numFloat = float(input("Digite um número real: "))

a = (numInteger1*2) * (numInteger2/2)
b = (numInteger1*3) + numFloat
c = numFloat**3

print(f"Valor da conta A: {a}")
print("Valor da conta B: {:.2f}".format(b))
print("Valor da conta C: {:.2f}".format(c))