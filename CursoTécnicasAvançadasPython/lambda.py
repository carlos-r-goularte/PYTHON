def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp-32) * 5/9

def main():
    temp_c = [0,12,34,100]
    temp_f = [32,65,100,212]

    #funções tradicionais para converter as temperatura
    print(list(map(fahrenheit_to_celsius,temp_f)))
    print(list(map(celsius_to_fahrenheit,temp_c)))


    #função lambda para converter as temperaturas

    print(list(map(lambda t: (t * 9/5) + 32, temp_c)))
    print(list(map(lambda t: (t-32) * 5/9, temp_f)))


if __name__ == "__main__":
    main()