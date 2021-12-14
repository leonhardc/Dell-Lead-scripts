from datetime import date
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10',
'12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

# convertendo datas
list_format = ["%d/%m/%Y", "%d de %B de %Y", "%d/%b/%Y", "%Y-%B-%d", "%d %B %Y"]

niver1 = datetime.strptime(aniversarios[0], list_format[0])
niver2 = datetime.strptime(aniversarios[1], list_format[1])
niver3 = datetime.strptime(aniversarios[2], list_format[2])
niver4 = datetime.strptime(aniversarios[3], list_format[3])
niver5 = datetime.strptime(aniversarios[4], list_format[4])
niver6 = datetime.strptime(aniversarios[5], list_format[1])
niver7 = datetime.strptime(aniversarios[6], list_format[0])


conv_niver = [niver1, niver2, niver3, niver4, niver5, niver6, niver7]

# ordenando as datas de aniversario
ord_niver = sorted(conv_niver, key=lambda a: (a.month, a.day))

# exibindo se existe alguém que aniversaria hoje
# primeiro teste
# hoje = datetime.now()
# segundo teste
hoje = niver1.replace(year=2021)

for item in ord_niver:
    if item.day == hoje.day and item.month == hoje.month:
        saida = hoje.strftime("Hoje, %A, %d de %B de %Y, tem aniversário!")
        print(saida)

