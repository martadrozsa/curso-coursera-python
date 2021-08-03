#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
# Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

n = int(input("Enter number: "))

i = 2

if n <= 1:
    print("It's not a prime number")
    # finalizar
else:
    prime = True
    for num in range(2, n - 1):
        if n % num == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not prime number")