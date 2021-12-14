import numpy as np
"""         Parte 1 - Oficina da Aula 3"""
visualizacao_stories = [
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
]

pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

# conversão de dados
visualizacao_stories = np.array(visualizacao_stories)
pessoas = np.array(pessoas)
dias_semana = np.array(dias_semana)

# Qual a media de visualizações por dia dessas pessaoas?
media_visualizacoes = visualizacao_stories.mean(axis=1)

# Qual o dia que teve mais visualizações de stories somadas?
dia_mais_visu = visualizacao_stories.sum(axis=0)
indice_mv = np.nonzero(dia_mais_visu == dia_mais_visu.max())

# Quem foi que teve o maior número de visualizações na última semana?
soma_visu = visualizacao_stories.sum(axis=1)
indice_pmv = np.nonzero(soma_visu == soma_visu.max())

# Impressão de dados

print("="*100)
print("Dados da Semana Passada")
print("-"*100)
print("Media de Visualizações por pessoa:")
for pessoa, media in zip(pessoas, media_visualizacoes):
    print(f"{pessoa} : {media:.2f}")

print(f"Dia da semana com mais visualizações somadas: {dias_semana[indice_mv]}")
print(f"Quem teve maior numero de visualizações ultima semana foi: {pessoas[indice_pmv]}")

print("="*100)

"""          Parte 2 - Oficina da Aula 3"""

visualizacao_stories_invalidos = np.array([
    [52, 68, 97, 55, -1, 98, -1],
    [53, -1, 38, -1, -1, 72, 49],
    [88, -1, 64, -1, 77, 130, 43],
    [-1, 30, -1, -1, -1, 182, -1],
    [41, 20, 33, -1, 37, 23, 7]
])
# conversao de dados, aplicando a mascara
array_mascarado = np.ma.masked_where(visualizacao_stories_invalidos == -1, visualizacao_stories)

# Qual a media de visualizações por dia dessas pessaoas?
media_visualizacoes = visualizacao_stories_invalidos.mean(axis=1)

# Qual o dia que teve mais visualizações de stories somadas?
dia_mais_visu = visualizacao_stories_invalidos.sum(axis=0)
indice_mv = np.nonzero(dia_mais_visu == dia_mais_visu.max())

# Quem foi que teve o maior número de visualizações na última semana?
soma_visu = visualizacao_stories_invalidos.sum(axis=1)
indice_pmv = np.nonzero(soma_visu == soma_visu.max())

# Impressão de dados

print("="*100)
print("Dados dessa Semana")
print("-"*100)
print("Media de Visualizações por pessoa:")
for pessoa, media in zip(pessoas, media_visualizacoes):
    print(f"{pessoa} : {media:.2f}")

print(f"Dia da semana com mais visualizações somadas: {dias_semana[indice_mv]}")
print(f"Quem teve maior numero de visualizações ultima semana foi: {pessoas[indice_pmv]}")

print("="*100)