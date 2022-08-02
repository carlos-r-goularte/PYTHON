height = float(input("Informe sua altura: "))
sex = input("Masculino/Feminino? [M/F]: ").upper()


idealWeightMale = (72.7*height) - 58
idealWeightFemale = (62.1*height) - 44.7

if sex == 'M':
    print("Peso ideal: {:.2f}".format(idealWeightMale))
elif sex == 'F':
    print("Peso ideal: {:.2f}".format(idealWeightFemale))
else:
    print("Digite corretamente!")