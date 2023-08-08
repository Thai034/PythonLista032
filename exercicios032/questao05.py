'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

print("Vamos brincar de calcular? Coloque abaixo 2 námeros")

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

resul1 = num1 + num2
resul2 = num1 - num2
resul3 = num2 - num1
resul4 = num1 * num2
resul5 = num1 / num2
resul6 = num2 % num1

print("Soma dos dois números: ", resul1)
print("Subtração do primeiro pelo segundo número: ", resul2)
print("Subtração do segundo pelo primeiro número: ", resul3)
print("Multiplicação entre os dois números: ", resul4)
print("Divisão do primeiro pelo segundo número: ", resul5)
print("Divisão do primeiro pelo segundo número: ", resul6)