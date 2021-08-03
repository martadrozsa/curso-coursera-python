# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.

user_number = int(input("Enter number: "))

n = user_number
count = 0
control = 1

while count < n:
    print(control)
    count = count + 1
    control = control + 2