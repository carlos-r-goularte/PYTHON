weight = float(input("Peso(kg) medido: "))

LIMIT = 50.0
excess = 0.0
assessment = 0.0

if weight > LIMIT:
    excess = weight-LIMIT
    assessment = excess * 4.00

print("Peso medido: {:.2f}kg   ||   Excedido: {:.2f}kg   ||   Multa: R${:.2f}".format(weight,excess,assessment))