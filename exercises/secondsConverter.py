segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
#entrada do usuario com o total de segundos
total_segs = int(segundos_str)
#converte a string em um inteiro e guarda em uma nova variável


horas = total_segs // 3600
#para saber quantas horas existem na quantidade de segundos do input
#faz uma divisão inteira do valor do input por 3600 que é o valor de segundos em 1 hora
#guarda este  valor na variável horas

segs_restantes = total_segs % 3600
#para saber os segundos restantes, depois da divisão inteira (número de horas), pega o resto da divisão
#a variável total_segs guarda o resto da divisão de 3600

minutos = segs_restantes // 60
#depois pode ser calculado os minutos
#divisão inteira do que sobrou dos segundos por 60 (valor de quantos segundos tem em 1 minuto)

segs_restantes_final = segs_restantes % 60
#para saber os segundos restantes

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")