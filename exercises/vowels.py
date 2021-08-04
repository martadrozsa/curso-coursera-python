# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(letter):
    if letter == "a" or letter == "A" or letter == "e" or letter == "E" or letter == "i" or letter == "I" or letter == "o" or letter == "O" or letter == "u" or letter == "U":
        return True
    else:
        return False

user_letter = input("Enter letter: ")

ret = vogal(user_letter)
print(ret)
