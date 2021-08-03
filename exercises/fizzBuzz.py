# Receba um número inteiro na entrada e imprima: FizzBuzz na saída se o número for divisível por 3 e por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.


number = int(input("Enter number: "))

remainder = number % 3
is_divisible_for3 = remainder == 0

remainder = number % 5
is_divisible_for5 = remainder == 0



if is_divisible_for3 and is_divisible_for5:
    print("FizzBuzz")


else:
    print(number)