# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética

grade1 = input("Enter the first grade: ")

grade2 = input("Enter the second grade: ")

grade3 = input("Enter the third grade: ")

grade4 = input("Enter the fourth grade: ")

number_grade1 = int(grade1)
number_grade2 = int(grade2)
number_grade3 = int(grade3)
number_grade4 = int(grade4)

arithmetic_mean = (number_grade1 + number_grade2 + number_grade3 + number_grade4) / 4

print("The arithmetic mean is", arithmetic_mean)