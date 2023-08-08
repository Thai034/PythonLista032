'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
'''

print("Posso calcular suas prestações, basta responder as perguntas abaixo:")

valor = float(input("Qual é o valor da compra? "))
prestacao = float(input("Qual é o numero de prestações? "))
resultado = valor / prestacao

print(f"O valor de cada uma das {prestacao:.0f} prestações será de R$ {resultado:.2f}")