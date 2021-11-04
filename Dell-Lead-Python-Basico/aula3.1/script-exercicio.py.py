def formatar_data(data):
    # formara data no formato dd/mes/aaaa
    meses = ['jan', 'fev', 'mar', 'mai', 'jun', 'jul', 'ago', 'set', 'out',
    'nov', 'dez']

    ano, mes, dia = data
    if 1 <= mes <= 12 and 1 <= dia <= 31:
        return '{}/{}/{}'.format(str(dia),meses[mes-1],str(ano))
    else:
        return None
    # fim de formatar_data

def formatar_hora(hora):
    # formata hora para 'hh:mm'
    hora, minutos = hora
    if 0 <= hora <= 24 and 0 <= minutos <= 60:
        return '{}:{}'.format(hora, minutos)
    else:
        return None

def eh_maior(data_testada, data_teste):
    # para simplificar a operação entre datas maiores do que as outras, eu acabei
    # criando essa função como auxiliar
    ano1, mes1, dia1 = data_testada
    ano2, mes2, dia2 = data_teste
    if ano1 > ano2:
        return True
    elif ano1 == ano2 and mes1 > mes2:
        return True
    elif ano1 == ano2 and mes1 == mes2 and dia1 >= dia2:
        return True
    else:
        return False


def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
    # imprime eventos da agenda no formato data_formatada - hora_formatada: evento
    for item in eventos:
        data, hora, evento = item
        if eh_maior(data, de_data) and eh_maior(ate_data, data):
            print('{} - {}: {}'.format(formatar_data(data), formatar_hora(hora), evento))

agenda = [

  ((2020, 1, 13), (11, 50), 'Renovar identidade'),

  ((2020, 1, 15), (16, 30), 'Fazer compras'),

  ((2020, 1, 25), (8, 45), 'Autenticar documentos'),

  ((2020, 2, 29), (14, 15), 'Prestar concurso'),

  ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),

  ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista'), ]

print('Primeira Impressão')
imprimir_eventos(agenda, (2020, 1, 20))

print('Segunda Impressão')
imprimir_eventos(agenda, ate_data=(2020, 3, 15))
