# Ex1010) Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 
# e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

#ENTRADA
#Usaremos split.() porque precisamos inserir mais de um dado numa mesma linha, e esse método permite tal ato.
#Podemosa agora receber um texto com todos os valores separados por espaço em branco.
TCP1, TQP1, TVP1 = input("").split(" ")

CP1 = int(TCP1)
QP1 = int(TQP1)
VP1 = float(TVP1)

TCP2, TQP2, TVP2 = input("").split(" ")

CP2 = int(TCP2)
QP2 = int(TQP2)
VP2 = float(TVP2)

#PROCESSAMENTO
VT = (QP1 * VP1) + (QP2 * VP2)

#SAIDA
print("Valor a pagar: R$ %.2f" % VT)