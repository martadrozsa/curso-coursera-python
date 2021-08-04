# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve 'Fizz'
# se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Caso o número não seja divisível 3 e também não seja divisível por 5, ela
# deve devolver o número recebido como parâmetro.

def fizzbuzz(number):
    is_divisible_for3 = number % 3 == 0
    is_divisible_for5 = number % 5 == 0

    if is_divisible_for3 and not is_divisible_for5:
        return "Fizz"

    elif is_divisible_for5 and not is_divisible_for3:
        return "Buzz"

    elif is_divisible_for3 and is_divisible_for5:
        return "FizzBuzz"

    else:
        return number


number = int(input("Enter number: "))

res = fizzbuzz(number)
print(res)
