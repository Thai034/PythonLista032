'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
'''

print("Se quer calcular seu salario mais sua comissão, então responda as perguntas abaixo:")
nome = input("Qual é o seu nome? ")
salario = float(input("Qual é o seu salário? "))
comissao = float(input("Quanto é o total de vendas em dinheiro? "))

resultado1 = comissao * 0.15
resultado2 = resultado1 + salario

print("nome: ", nome)
print("salário fixo: ", salario)
print("comissao: ", resultado1)
print("Salário complexo: ", resultado2)