# Ex1009) Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este 
# vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

#ENTRADA
Nome = str(input(""))
SF = float(input(""))
TV = float(input(""))

#PROCESSAMENTO
STotal = (SF + (TV * 0.15))

#SAIDA
print("Total = R$ %.2f" % STotal)