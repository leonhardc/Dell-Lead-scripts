import itertools

Camisas = ['Camisa Azul', 'Camisa Verde', 'Camisa Vermelha']
Calcas = ['Calça Branca', 'Calça Amarela', 'Calça Azul']

for opcao in list(itertools.product(Camisas, Calcas)):
    print(opcao)