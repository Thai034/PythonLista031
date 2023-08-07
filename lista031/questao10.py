'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''

print("Posso calcular sua prestação atrasada, para isso preciso que me informe valor, taxa e tempo em dias")

valor = float(input("Qual o valor normal da prestação? "))
taxa = float(input("Qual sua taxa de juros? "))
tempo = float(input("Quantos dias de atraso? "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor da sua prestacao em atraso é: ", prestacao, "R$")