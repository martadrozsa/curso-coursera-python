# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como
# parâmetro e devolve o maior número primo menor ou igual ao número passado à função

def is_prime(n):
    prime = True
    for num in range (2, n- 1):
        if n % num == 0:
            prime = False
            break

    return prime


def maior_primo(num):
    while not is_prime(num):
        num = num - 1

    return num


user_number = int(input("Enter number: "))

print(maior_primo(user_number))