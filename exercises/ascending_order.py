# Verificando ordenação
# Receba 3 números inteiros na entrada e imprima:
# crescente (se eles forem dados em ordem crescente).
# Caso contrário, imprima: não está em ordem crescente

number = []

user_number1 = int(input("Enter your first number: "))
number.append(user_number1)
user_number2 = int(input("Enter your second number: "))
number.append(user_number2)
user_number3 = int(input("Enter your third number: "))
number.append(user_number3)


if user_number1 < user_number2 and user_number2 < user_number3:
    print("Ascending order")
else:
    print("Is not in ascending order")
