'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

print("Quer descobrir o valor de venda de um produto? Responda aqui qeu eu farei isso por você:")

valor= float(input("Qual é o preço do produto? "))
percentual = float(input("Qual é o percentual? "))

resultado1 = valor + (valor * (percentual / 100))

print("O produto sairá por R$:", resultado1)