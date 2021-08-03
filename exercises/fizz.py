# Receba um número inteiro na entrada e imprima: Fizz (se o número for divisível por 3)
# Caso contrário, imprima o mesmo número que foi dado na entrada.


number = int(input("Enter number: "))

remainder = number % 3
is_divisible = remainder == 0


if is_divisible:
    print("Fizz")
else:
    print(number)
