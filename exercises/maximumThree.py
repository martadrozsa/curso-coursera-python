#Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a
# receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1

    elif num2 > num3:
        return num2

    else:
        return num3


num1 = int(input("Enter first number: "))

num2 = int(input("Enter first number: "))

num3 = int(input("Enter third number: "))

res = maximo(num1, num2, num3)

print(res)