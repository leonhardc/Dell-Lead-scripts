# avalia a musica em boa, mediana ou ruim
def avalia(musica):

    if 0 <= musica <= 1:
        return 'ruim'
    if 2 <= musica <= 3:
        return 'mediana'
    if 4 <= musica <= 5:
        return 'boa'

# retona qual genero tem mais musicas boas
def retorna_maior(pop, rock):
    if pop > rock:
        return 'Pop'
    elif rock > pop:
        return 'Rock'
    else:
        return 'Ambos os gêneros tem a mesma quantidade de musicas boas.'

# listas de notas
notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# listas de avaliações (ruim, mediana, boa)
avaliacao_rock = list(map(avalia, notas_rock))
avaliacao_pop = list(map(avalia, notas_pop))

# quantidade de musicas boas, medianas e ruins em cada categoria
qt_music_ruins_rock = len(list(filter(lambda x: x == 'ruim', avaliacao_rock)))
qt_music_medianas_rock = len(list(filter(lambda x: x == 'mediana', avaliacao_rock)))
qt_music_boas_rock = len(list(filter(lambda x: x == 'boa', avaliacao_rock)))

qt_music_ruins_pop = len(list(filter(lambda x: x == 'ruim', avaliacao_pop)))
qt_music_medianas_pop = len(list(filter(lambda x: x == 'mediana', avaliacao_pop)))
qt_music_boas_pop = len(list(filter(lambda x: x == 'boa', avaliacao_pop)))

# existe alguma musica mediana de rock?
exist_mediana = any(list(map(lambda x: x == 'mediana', avaliacao_rock)))
exist_mediana = 'Sim' if exist_mediana == True else 'Não'

# todas as musicas de pop são boas?
todas_sao_boas = all(list(map(lambda x: x == 'boa', avaliacao_pop)))
todas_sao_boas = 'Sim' if todas_sao_boas == True else 'Não'

# qual genero tem mais musicas boas?
str_melhor = retorna_maior(qt_music_boas_pop,qt_music_boas_rock)


# saida de dados

str_sRock = """
Genero: Rock
    Musicas Boas: {}
    Musicas Medianas: {}
    Musicas Ruins: {}
""".format(qt_music_boas_rock, qt_music_medianas_rock, qt_music_ruins_rock)

str_sPop = """
Genero: Pop
    Musicas Boas: {}
    Musicas Medianas: {}
    Musicas Ruins: {}
""".format(qt_music_boas_pop, qt_music_medianas_pop, qt_music_ruins_pop)

str_sComp = """
Existe alguma musica mediana no genero Rock? {}
Todas as musicas de Pop são Boas? {}
Que genero musical tem mais musicas boas? {}
""".format(exist_mediana, todas_sao_boas, str_melhor)

print(str_sRock)
print(str_sPop)
print(str_sComp)
