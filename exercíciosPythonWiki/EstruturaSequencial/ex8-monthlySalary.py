hourlyWage = float(input("Digite o quanto você ganha por hora: R$"))

hourWorkedPerDay = int(input("Quantas horas de trabalho por dia?: "))

salary = hourlyWage*hourWorkedPerDay*22

print("Salário mensal: R${:.2f}".format(salary))