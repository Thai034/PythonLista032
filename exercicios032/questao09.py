'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

print("Quer saber quantos anos em dias você tem? Ta bom, responda as perguntas abaixo:")

anos = int(input("Quantos anos você tem? "))
meses = int(input("Quantos meses ja passou desde o seu último aniversário? "))
dias = int(input("Quantos dias ja faz do seu último aniversário? "))

resultado = (anos * 365) + (meses * 30) + dias
print("Você tem", resultado, "dias de vida")
