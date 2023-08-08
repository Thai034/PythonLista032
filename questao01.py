'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

print("Coloque aqui sua conta do restaurante, que calcularemos com os 10% do garçom.")
num = float(input("Valor da sua conta: "))

res = num + (num * 0.10)
print("O total que você precisará pagar sera: ", res)

