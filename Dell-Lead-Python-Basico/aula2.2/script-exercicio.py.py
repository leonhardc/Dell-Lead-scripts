"""
    Este programa exibe o resultado de uma pesquisa sobre a escolha de que curso o pesquisador deveria fazer,
    de acordo com as respostas de seus amigos
"""
cursos = [
  'Engenharia de Software',
  'Python para Data Science',
  'Introdução a Java'
]

respostas = [1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
  1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
  2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1
]

# Primeira etapa: contagem de votos

cont_EngSoft = 0
cont_PyDS = 0
cont_IntJava = 0 
totalVotos = len(respostas)

for resposta in respostas:
    if resposta == 0: # Engenharia de Software
        cont_EngSoft += 1
        
    if resposta == 1: # Python para Data Science
        cont_PyDS += 1
        
    if resposta == 2: # Introdução a Java
        cont_IntJava =+ 1

mais_votos = max([cont_EngSoft, cont_PyDS, cont_IntJava])

# Apresentando Resultados
print('RESULTADOS')
print('Curso                        Total de Votos       Porcentagem')
print(cursos[0], '     ',cont_EngSoft, '                 ',(cont_EngSoft/totalVotos)*100, '%')
print(cursos[1], '   ',cont_PyDS, '                 ',(cont_PyDS/totalVotos)*100, '%')
print(cursos[2], '          ',cont_IntJava, '                  ',(cont_IntJava/totalVotos)*100, '%')
print()
print('CURSO VENCEDOR: ', end = '')

if cont_EngSoft == mais_votos: # curso vencedor é Engenharia de Software
    print(cursos[0])
    
if cont_PyDS == mais_votos: # curso vencedor é Python para Data Science
    print(cursos[1])
    
if cont_IntJava == mais_votos: # curso vencedor é Introdução a Java
    print(cursos[2])
    
