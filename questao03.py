'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

print("Aqui informaremos seu peso em gramas e sua altura em cenímetros, basta responder as seguintes pergntas:")
peso = float(input("Informe aqui seu peso em Kg: "))
alt = float(input("Informe aqui sua altura em metros: "))

resultado1 = alt * 100
resultado2 = peso * 1000

print("O resultado do seu peso em gramas é: ", resultado1)
print("O resultado da sua altura em centímetros é: ", resultado2)