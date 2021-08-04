# Escreva um programa que receba um número inteiro na entrada e
# verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima "sim"; se não existir, imprima "não".


user_number = input("Enter the number to check if it has an adjacent digit: ")

adjacent = False

for idx, digit in enumerate(user_number):
    if idx +1 >= len(user_number):
        break

    if user_number[idx] == user_number[idx +1]:
        adjacent = True
        break


if adjacent == False:
    print("não")
else:
    print("sim")