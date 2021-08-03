#Receba um número inteiro na entrada e imprima: par (quando o número for par)
# ou imprima: ímpar (quando o número for ímpar)

numText = input("Enter a number: ")
num = int(numText)

if num % 2 == 0:
    print("Even number")

else:
    print("Odd number")
