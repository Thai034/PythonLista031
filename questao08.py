'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

print("Informe sua distancia que calcularei quantos litros você gastará nessa viagem: ")

dist = float(input("informe a distancia da viagem? "))
litro = float(input("Quantos quilometros seu carro percorre a cada litro? "))

resultado = dist / litro

print("Seu carro irá precisar de: ", resultado, "litros pra percorrer a viagem")