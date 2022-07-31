maxDigit = input("maxDigit: ")


strMaxDigit = str(maxDigit) * 4

for digit in range(1000,int(strMaxDigit)+1,1):
    strDigit = str(digit)
    listDigit = list(strDigit)

    if int(listDigit[0]) <= int(maxDigit):
        value0 = int(listDigit[0])
    else:
        value0 = 0

    if int(listDigit[1]) <= int(maxDigit):
        value1 = int(listDigit[1])
    else:
        value1 = 0
    
    if int(listDigit[2]) <= int(maxDigit):
        value2 = int(listDigit[2])
    else:
        value2 = 0

    if int(listDigit[3]) <= int(maxDigit):
        value3 = int(listDigit[3])
    else:
        value3 = 0

    sum = value0 + value1 + value2 + value3

    if sum == 21:
        print(digit)
    else:
        print("null")