"""
O módulo itertools utiliza-se de técnicas de programação funcional, como as funções geradoras,
que são funções que retornam um objeto iterável. Esse objeto iterável não possui um valor fixo,
ou seja, quando invocado, um novo valor é computado, como você pode observar no exemplo a seguir:


No exemplo apresentado, você pode notar que a função count retorna um iterador. A variável chamada
‘contador’ recebe esse iterador e, à medida que é invocada, por meio da função next, é computado um
novo valor a essa variável. Com isso, esse valor é computado somando mais 1 ao valor anterior e tendo
um mesmo comportamento de um iterador qualquer dentro de um ForLoop

"""

import itertools
contador = itertools.count()

print(contador) # count(0)
print(next(contador)) # 0
next(contador)
print(next(contador)) # 2

print('*'*50)

"""
Análises combinatórias são muito poderosas e podem auxiliar em diversos tipos de problemas. Essas análises 
são bastante utilizadas em estatística e, como você sabe, estatística é uma das competência necessárias de 
um cientista de dados. Observe o código a seguir para conhecer exemplos de como utilizar o método combinations 
para fazer combinações.

"""

import itertools

print(itertools.combinations("ABC",2)) # <itertools.combinations at 0x1916522f130>

print(list(itertools.combinations("ABC",2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("AABC",2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("ABCD",3)))
# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]

print('*'*50)

"""
Permutação é um dos assuntos discutidos na disciplina de análise combinatória e é uma técnica de contagem 
utilizada para determinar quantas maneiras existem para ordenar os elementos de um conjunto finito.

O método permutations, utilizado para fazer permutações, trata todos os elementos como únicos, baseado em 
suas posições, e não em seus valores. O parâmetro r é o tamanho da permutação e, se não especificado, ele 
é definido como o comprimento da lista de entrada. O próximo código demonstra como fazer permutações utilizando 
o método permutations. Confira:

"""

import itertools

print(list(itertools.permutations([1,1]))) # [(1, 1), (1, 1)]

print(list(itertools.permutations([1, 2]))) # [(1, 2), (2, 1)]

print(list(itertools.permutations([1, 2, 3])))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(itertools.permutations([1, 2, 3],r=2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print('*'*50)

"""
O produto cartesiano é o conjunto de todos os pares ordenados (x,y), tais que x pertence ao conjunto A e y pertence 
ao conjunto B, onde a ordem interfere na elaboração do conjunto, como mostra a figura a seguir.

"""

import itertools

print(list(itertools.product([1, 2], repeat=2))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product([1, 2], [1, 2]))) # [(1, 1), (1, 2), (2, 1), (2, 2)]

print(list(itertools.product(['Python'], ['Academy', 'Rocks'])))
# [('Python', 'Academy'), ('Python', 'Rocks')]

print(list(itertools.product([1, 2], [3, 4], [5, 6])))
# [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

print('*'*50)

"""

"""