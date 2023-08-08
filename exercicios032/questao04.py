'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''
import math

print("Quer saber seu IMC (indice de massa corporal)? Coloque suas informações aqui em baixo que lhe diremos!")

#Fórmula: IMC = peso / altura2

peso = float(input("coloque aqui seu peso. OBS: em Kg: "))
altura = float(input("Coloque aqui sua Altura. OBS: em metros: "))

IMC = peso / math.pow(altura,2)

print("Seu IMC é igual a", IMC)