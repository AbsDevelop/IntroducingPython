# Ex1006) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a 
## nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

#ENTRADA
A = float(input(""))
B = float(input(""))
C = float(input(""))

#PROCESSAMENTO
MEDIA = (A * 2 + B * 3 + C * 5) / 10

#SAIDA
print("MEDIA = %.1f" % MEDIA)