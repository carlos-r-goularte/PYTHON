hourlyWage = float(input("Quando você ganha por hora: R$"))
workedHours = int(input("Horas trabalhadas: "))

grossSalary = ((workedHours*5)*4)*hourlyWage

IR = 0.11
INSS = 0.08
SINDICATO = 0.05
netSalary = 0

incomeTax = grossSalary * IR
socialInsurance = grossSalary * INSS
syndicate = grossSalary * SINDICATO

netSalary = grossSalary - incomeTax - socialInsurance - syndicate

print(f'''Salário Bruto R${grossSalary:.2f} | IR: R${incomeTax:.2f} | INSS: R${socialInsurance:.2f} | Sindicato: R${syndicate:.2f} | Salário Líquido: R${netSalary:.2f}''')