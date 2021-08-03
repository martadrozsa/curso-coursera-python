# Escreva um programa que receba um número inteiro na entrada, calcule e
# imprima a soma dos dígitos deste número na saída

user_number = int(input("Enter number: "))

n = user_number
sum = 0


while n > 0:
    digit = n % 10
    sum = sum + digit
    n = (n - digit) // 10

print(sum)
