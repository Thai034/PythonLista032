'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia
'''

print("Quer saber quantos minutos se passou desde às 00:00h, até agora? Vamos descobrir!")
hora = int(input("Coloque por favor as horas, ex: são 09:30 = 9: "))
mim = int(input("coloque o valor dos minutos: "))

hora1 = hora * 60
hora2 = hora1 + mim

print("De 00:00h até agora já se passaram", hora2, "minutos")