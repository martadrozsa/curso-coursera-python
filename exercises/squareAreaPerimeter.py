# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
# calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"


lado_quadrado = int(input("Digite o valor correspondente ao lado de um quadrado: "))

perimetro = lado_quadrado * 4

area = lado_quadrado ** 2

print("perímetro:", perimetro, "- área:", area)
