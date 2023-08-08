'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

print("Quer saber o percentual de seus eleitores? Responda as perguntas abaixo e responderei para você!")

eleitores = int(input("Informe o numero de eleitores do municipio: "))
brancos = int(input("Informe o número total de votos brancos: "))
nulos = int(input("Informe o numero total de votos nulos: "))
validos = int(input("informe o numero total de votos válidos: "))


print(f"Votos totais: {eleitores}%")
print(f"Votos Brancos: {100 * brancos/eleitores:.2f}%")
print(f"Votos nulos: {100 * nulos/eleitores:.2f}%")
print(f"Votos válidos: {100 * validos/eleitores:.2f}%")