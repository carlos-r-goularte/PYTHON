import enum
from pydoc import stripid
from tkinter.messagebox import RETRYCANCEL


dias = ("Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado")
dias_en = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

iterador_dias = iter(dias)

print(next(iterador_dias))
print(next(iterador_dias))
print(next(iterador_dias))

#utlizar a função para percorer um arquivo
print()
with open("dados.txt",'r') as fp:
    for linha in iter(fp.readline,""):
        print(linha)
        
#iterador tradicional (range)
print()
for i in range(len(dias_en)):
    print(i,dias_en[i])

#função enumerate
print()
for i, dia in enumerate(dias):
    print(i,dia)

#função zip
print()
for d in zip(dias,dias_en):
    print(d)


#combinação fundção zip com enumerate
print()
for i,dia in enumerate(zip(dias,dias_en)):
    print(f"{i} - {dia[0]} em inglês: {dia[1]}")

