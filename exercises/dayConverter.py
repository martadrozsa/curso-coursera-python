#Escreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
# faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
# A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
#entrada do usuario com o total de segundos

total_segs = int(segundos_str)
#converte a string em um inteiro e guarda em uma nova variável


dia = total_segs // 86400 #descobrir os dias
#para saber a quantidade de dias com divisão inteira em relação ao valor de segundos do input


segs_restantes_depois_dia = total_segs % 86400
#divisão para saber o resto de segundos da divisão anterior (total de dias)


horas = segs_restantes_depois_dia // 3600 #descobrir as horas
#para saber quantas horas existem na quantidade de segundos que sobrou da divisão para saber os dias
#divisão inteira do valor na variável segs_restantes_dia por 3600 que é o valor de segundos em 1 hora


segs_restantes_depois_horas = total_segs % 3600
#para saber os segundos restantes, depois da divisão inteira (número de horas), pega o resto da divisão
#a variável total_segs guarda o resto da divisão de 3600


minutos = segs_restantes_depois_horas // 60 # descobrir os minutos
#depois pode ser calculado os minutos
#divisão inteira do que sobrou dos segundos por 60 (valor de quantos segundos tem em 1 minuto)


segs_restantes_depois_minutos = segs_restantes_depois_horas % 60 # descobrir os segundos
#para saber os segundos restantes depois de saber os minutos


print(dia, "dia(s),", horas, "hora(s), ", minutos, "minuto(s) e", segs_restantes_depois_minutos, "segundo(s).")