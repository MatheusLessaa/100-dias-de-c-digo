def calculadora():
    while True:
            print ("Escolha a operação a ser realizada")
            print ("(1)Soma")
            print ("(2)Subtracao")
            print ("(3)Multiplicacao")
            print ("(4)Divisao")
            escolha = int(input("Digite qual operação deseja realizar"))

            if escolha == 1:
                num1 = int(input("Digite o primeiro numero a ser somado "))
                num2 = int(input("Digite o segundo numero a ser somado "))
                result = num1+num2
                print("o resultado é" ,result)

            if escolha == 2:
                num1 = int(input("Digite o primeiro numero a ser subtraido "))
                num2 = int(input("Digite o segundo numero a ser subtraido "))
                result = num1-num2
                print("o resultado é" ,result)

            if escolha == 3:
                num1 = int(input("Digite o primeiro numero a ser multiplicado "))
                num2 = int(input("Digite o segundo numero a ser multiplicado "))
                result = num1*num2
                print("o resultado é" ,result)

            if escolha == 4:
                num1 = int(input("Digite o dividendo "))
                num2 = int(input("Digite o divisor "))
                if num2 == 0:
                    print("Um número não pode ser dividido por 0")
                else:
                    result = num1/num2
                    print("o resultado é" ,result)

            if escolha >4:
                print("opção inválida!")

            keep = input("Deseja continuar? (s/n)")
            if keep =="n":
                print("Calculadora encerrada")
                break

calculadora()