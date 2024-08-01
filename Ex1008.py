# Ex1008) Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse 
# funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

#ENTRADA
NF = int(input(""))
NHT = int(input(""))
VH = float(input(""))

#PROCESSAMENTO
SALARIO = (NHT * VH)

#SAIDA
print("Número =", NF)
print("Salário = R$ %.2f" % SALARIO)