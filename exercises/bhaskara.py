# Escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros  a a,  b b, e  c c da equação  ax2 + bx + c ax2 +bx+c,
# respectivamente, e imprimir o resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima: esta equação não possui raízes reais
# Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima: a raiz desta equação é X
# ou a raiz dupla desta equação é X (onde X é o valor da raiz dupla)
# Quando houver duas raízes reais imprima: as raízes da equação são X e Y (onde X e Y são os valor das raízes).
# No caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente.
# Exemplos: as raízes da equação são 1.0 e 2.0  e  as raízes da equação são -2.0 e 0.0


import math

a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    root1 = (- b + math.sqrt(delta)) / (2 * a)
    print("The square root of that equation is", root1)
else:
    if delta < 0:
        print("This equation has no real roots")
    else:
        root1 = (- b + math.sqrt(delta)) / (2 * a)
        root2 = (- b - math.sqrt(delta)) / (2 * a)
        if root1 > root2:
            print("the roots of the equation are", root2, "e", root1)
        else:
            print("the roots of the equation are", root1, "e", root2)