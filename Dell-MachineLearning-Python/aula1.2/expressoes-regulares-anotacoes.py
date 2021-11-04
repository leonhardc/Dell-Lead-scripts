"""
ao utilizar regex, vamos sempre usar a letra r antes da string. O r indica que a string é bruta, desse modo não
serão considerados caracteres especiais. Sem o r, a barra invertida (backslash) ‘\’ faria com que o caractere que
vem a seguir fosse considerado um caractere especial. Como é mostrado no código seguinte, com e sem o r como prefixo
da string:

"""
import re

print('\tTabulação') # ‘ Tabulação’

print(r'\tTabulação') # ‘\tTabulação’

"""
Os métodos que vamos usar para trabalhar com expressões regulares (regex) em Python reside em um módulo denominado
re. Por enquanto, vamos nos concentrar no método search(). Esse método recebe como parâmetro uma expressão regular 
e uma string, e seu papel é fazer a varredura na string, procurando o primeiro local onde há uma correspondência do 
padrão regex que foi passado. O código a seguir demostra exemplos de utilização do método search.
 
"""



palavra = r'otorrinolaringologista 816'

print(re.search(r'rino', palavra)) # <re.Match object; span=(4, 8), match='rino'>

print(re.search(r'ri', palavra)) # <re.Match object; span=(4, 6), match='ri'>

print(re.search(r'rino', palavra).group(0)) # rino

print(re.search(r'100', palavra)) # None

"""
Vamos analisar um caso. Para isso, considere a lista de dados pessoais a seguir:

Laura Maria da Silva
(46) 93201-6392
(89) 42010-7411
(61) 47405-4895
Rua José Geraldo
lauramaria@hotmail.com
Le@d Dell Technologies

Como você faria para extrair os números de telefone com os seus respectivos DDDs, a partir da string apresentada? Bom, 
primeiro você deve tentar buscar somente o DDD de cada número. Confira isso no seguinte código:
"""


palavra = r"Laura Maria da Silva\n(46) 93201-6392\n(89) 42010-7411\n(61)47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d DellTechnologies"

print(re.search(r'[0-9][0-9]', palavra)) # <re.Match object; span=(23, 25), match='46'>

print(re.findall(r'[0-9][0-9]', palavra))
# ['46', '93', '20', '63', '92', '89', '42', '01', '74', '11', '61', '47', '40', '48', '95']

print(re.findall(r'\W[0-9][0-9]\W', palavra)) # ['(46)', '(89)', '(61)']

"""
Quanto mais padrões você coloca nas expressões regulares, maiores elas ficam. Para facilitar a criação das 
expressões, são utilizados quantificadores de repetição. Esses quantificadores possuem o papel de fazer com 
que os mecanismos das expressões regulares correspondam a uma determinada quantidade de ocorrências. A tabela 
a seguir associa um símbolo à quantidade de ocorrências que aquele símbolo representa. 

Para você entender melhor como utilizar os quantificadores, observe três exemplos de correspondência de DDD 
apresentados no seguinte código:
"""


print(re.findall(r'\W[0-9][0-9]\W', palavra)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\W[0-9]{2}\W', palavra)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\W\d{2}\W', palavra)) # ['(46)', '(89)', '(61)']

"""
Nas linhas 6, 8 e 10 dos exemplos apresentados, é mostrado o mesmo padrão utilizando símbolos diferentes:

    Na linha 6, criamos uma expressão regular sem utilizar quantificadores, repetindo o símbolo duas vezes 
    para achar a ocorrência duas vezes;
    
    Na linha 8, utilizamos o quantificador {2} para explicitar que queremos somente duas correspondências 
    dessa expressão, ou seja, dois dígitos. Não havendo a necessidade de repetir símbolos;
    
    Na linha 10, foi demonstrado que o caractere especial \d é equivalente ao caractere especial [0-9], 
    como o quantificador {2}.
"""

"""
Agora vamos trabalhar com um número telefônico completo. Como já temos a expressão que busca somente o DDD, 
vamos fazer agora a expressão que busca somente o número telefônico. O código a seguir demonstra qual expressão 
regular foi utilizada para reconhecer esse número. Observe:

"""

print(re.findall(r'\W\d{2}\W', palavra)) # ['(46)', '(89)', '(61)']

print(re.findall(r'\d{5}\W\d{4}', palavra)) # ['93201-6392', '42010-7411', '47405-4895']

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', palavra))
# ['(46) 93201-6392', '(89) 42010-7411', '(61) 47405-4895']


"""
Vamos utilizar a nova string que foi apresentada na tela anterior. Agora que não temos mais o DDD de um dos 
números telefônicos, se usássemos a expressão regular '\W\d{2}\W\s\d{5}\W\d{4}‘, apresentada no código anterior, 
só seriam retornados 2 dos 3 números contidos na nova string. Sabendo disso, vamos criar uma nova expressão que 
busca números telefônicos sem o DDD. O código a seguir mostra o retorno esperado de cada expressão regular:

"""

palavra = r"Laura Maria da Silva\n(46) 93201-6392\n42010-7411\n(61)47405-4895\nRua José Geraldo\nlauramaria@hotmail.com\nLe@d DellTechnologies"

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}', palavra)) # ['(46) 93201-6392', '(61) 47405-4895']

print(re.findall(r'\d{5}\W\d{4}', palavra)) # ['93201-6392', '42010-7411', '47405-4895']

print(re.findall(r'\W\d{2}\W\s\d{5}\W\d{4}|\d{5}\W\d{4}', palavra))
# ['(46) 93201-6392', '42010-7411', '(61) 47405-4895']

"""
Suponha que você possui uma empresa, mas por ser uma empresa recente, não há muitos clientes. 
Então, você decide enviar alguns e-mails para as pessoas, explicando quais serviços a sua empresa 
oferece. Infelizmente, você percebe que não possui lista de e-mails para que possa enviar um material 
de divulgação. De repente, você resolve procurar listas de e-mails na internet e encontra um texto contendo 
vários dados, inclusive e-mails de pessoas. Agora sua missão é extrair somente os e-mails que estão contidos 
nesse texto. Você consegue pensar em uma expressão regular que busca os e-mails válidos em uma string?

"""

palavra = r'contato@dellead.com, franciscojose@yahoo.com.br, ana.julia@universidade.edu,francisca-321-aline@meu-trabalho.net, Le@d Dell Technologies'

print(re.findall(r'[a-zA-Z0-9_.-]+@', palavra))
# ['contato@', 'franciscojose@', 'ana.julia@', 'francisca-321-aline@', 'Le@']

print(re.findall(r'@[a-zA-Z0-9-]+\.', palavra))
# ['@dellead.', '@yahoo.', '@universidade.', '@meu-trabalho.']

print(re.findall(r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', palavra))
# ['@dellead.com', '@yahoo.com.br', '@universidade.edu', '@meu-trabalho.net']

print(re.findall(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', palavra))
# ['contato@dellead.com', 'franciscojose@yahoo.com.br', 'ana.julia@universidade.edu',
# 'francisca-321-aline@meu-trabalho.net']