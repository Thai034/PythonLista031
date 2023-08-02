'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''

print("Coloque seu salário que calcularei seu aumento de 15%")
num = float(input("Seu salário: "))

res = num + (num * 0.10)
print("Seu salario com o aumento ficará: ", res)