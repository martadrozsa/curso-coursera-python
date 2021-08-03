# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

num = int(input("Digite um número inteiro: "))

digito = num // 10
digito_final = digito % 10

print("O dígito das dezenas é", digito_final)
