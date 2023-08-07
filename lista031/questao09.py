'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

print("Informe um número, que lhe direi seu quadrado e sua raiz")

num = float(input("informe seu número: "))

resultado1 = math.pow(num,2)
resultado2 = math.sqrt(num)

print(num)
print("O quadraro do seu número é: ", resultado1)
print("A raíz quadrado do seu número é: ", resultado2)