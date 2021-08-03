# Receba um número inteiro na entrada e imprima: Buzz (se o número for divisível por 5).
# Caso contrário, imprima o mesmo número que foi dado na entrada.

number = int(input("Enter number: "))

remainder = number % 5
is_divisible = remainder == 0


if is_divisible:
    print("Buzz")
else:
    print(number)
