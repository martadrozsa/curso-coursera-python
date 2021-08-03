# Escreva um programa que receba um número natural  n n na entrada e imprima  n! (fatorial) na saída

number = int(input("Enter a natural number: "))

n = number
factorial = number

while n - 1 > 0:
    factorial = factorial * (n - 1)
    n = n - 1

if number == 0:
    print("1")

else:
    print(factorial)
