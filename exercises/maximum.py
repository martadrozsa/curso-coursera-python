# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(num1, num2):
    if num1 > num2:
        return num1

    else:
        return num2


num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

res = maximo(num1, num2)

print(res)