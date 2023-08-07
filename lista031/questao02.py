'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

print("insira abaixo seus números para que calculemos a soma e multiplicação")
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

resul1 = num1 + num2 + num3
resul2 = num1 * num2 * num3

print("Resultado da soma: ", resul1)
print("Resultado da multiplicação: ", resul2)
