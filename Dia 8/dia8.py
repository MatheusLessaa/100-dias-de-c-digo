def conversão():
    temp = celsius*1.8 + 32
    print(temp)

while True:
    celsius = int(input("Por favor, digite a temperatura em celsius que deseja converter: "))
    conversão()

    keep = input("Deseja continuar? (s/n)")

    if keep !=  's':
        break