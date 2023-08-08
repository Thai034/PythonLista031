a = 3
b = -4

# Operadores Aritiméticos
soma = a + b
sub = a - b
mult = a * b
div = a / b
div_inteiros = a // b

print(f"Soma: { soma }")
print(f"Subtração: { sub }")
print(f"Multiplicação: { mult }")
print(f"Divisão: { div }")
print(f"Divisão de inteiros: { div_inteiros }")
print(f"Cálculos dentro do print: { a * b }")
print(f"Resto da divisão de 16 por a: { 16 % a }")

# Operador Relacional
print(f"a == b: { a == b }")
print(f"a < 5: { a < 5 }")
print(f"a > b: { a > b }")
print(f"a <= 3: { a <= 3 }")
print(f"a >= 4: { a >= 4 }")
print(f"a != b: { a != b }")

'''
== igual a
< Menor que
> Maior que
<= Menor ou igual
>= Maior ou igual
!= Diferente de
'''

c = a != b #Um "=" é igua a "recebe"
print(f"c: {c}")
print(f"tipo da var")

#Operadores Lógicos verdadeiro ou falso
'''
não (negação); not ;Operador de negação. Não VERDADEIRO = FALSO, e não FALSO = VERDADEIRO.
ou (disjunção); or ;Operador que resulta VERDADEIRO quando um de seus operandos lógicos for verdadeiro.
e (conjunção); and ;Operador que resulta em FALSO quando um de seus operandos lógicos for falso.
'''

logic1 = True
logic2 = False
print(f"type(logic1): {type(logic1)}")
print(f"type(logic2): {type(logic2)}")

print(f"logic1: {logic1}")
print(f"not logic1: {not logic1}")
print(f"logic1 or logic2: {logic1 or logic2}")
print(f"logic1 and logic2: {logic1 and logic2}")



