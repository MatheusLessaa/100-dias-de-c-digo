def tabuada():
    for i in range(11):
        print(num * i)

while True:
    num = int(input("Por favor, digite o número que deseja descobrir a tabuada: "))
    tabuada()

    keep = input("Deseja continuar? (s/n)")

    if keep !=  's':
        break