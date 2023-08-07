valor1 = 0.75317
valor2 = 73932.6
valor3 = 11.349

#formatação apenas como valor float
print("Valor 1: {:f}".format(valor1))

#formatação float com decimal em 2 digitos
print("Valor 1: {:.2f}".format(valor1))
print("Valor 2: {:.2f}".format(valor2))
print("Valor 3: {:.2f}".format(valor3))

#formatação float com separador de milhares e decimal em 2 digitos

print("Valor 2: {:,.2f}".format(valor2))

#---------------------------------------------------------------------------------
#Formatação fliat, com total de 10 digitos (numerps e ponto), sendo 2 decimais.
print("Valor 1: {:10.2f}".format(valor1))
print("Valor 2: {:10.2f}".format(valor2))
print("Valor 3: {:10.2f}".format(valor3))

#semelhante ao interior, mas preenche casas antes do ponto com zero quando necessário
print("Valor 1: {:010.2f}".format(valor1))
print("Valor 2: {:010.2f}".format(valor2))
print("Valor 3: {:010.2f}".format(valor3))