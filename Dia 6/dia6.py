num= int(input("Digite um número para saber sua fatorial "))
result=0


if num<1:
    print("Não existe um resultado para essa fatoração")
    quit= int(input("Digite para sair"))

if num==1:
    print("O resultado é 1")
    quit= int(input("Digite para sair"))

else:
    factor=num
    while num>=2: 
        factor = factor*(num-1)
        num -=1


print(factor)
quit= int(input("Digite para sair"))
