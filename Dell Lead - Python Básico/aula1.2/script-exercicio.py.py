
# Entrada de dados
nome = input('Digite seu nome >> ')
peso = input('Digite seu peso >> ')
altura = input('Digite sua altura >> ')

# processamento de dados
peso_float = float(peso)
altura_float = float(altura)

imc = peso_float/(altura_float*altura_float)

# saida de dados
print(nome, ' seu Indice de Massa Corporal (IMC) é ', imc)
