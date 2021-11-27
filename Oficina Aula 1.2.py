import re

logs = r""" 2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado 
            2020-05-11 00:09:52,532 | ERROR -> Erro não esperado 
            2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema 
            2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema 
            2020-05-11 20:46:35,271 | ERROR -> Erro não esperado 
            2020-05-12 08:14:59,895 | ERROR -> Erro não esperado 
            2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema 
            2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema 
            2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida 
            2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema 
            2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema 
            2020-05-15 08:40:33,776 | ERROR -> Erro não esperado 
            2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida """


def hora(horario):
    return horario[0:2]


erros = (re.findall(
    r'\d{2}\W\d{2}\W\d{2},\d{3}\W\|\WCRITICAL|\d{2}\W\d{2}\W\d{2},\d{3}\W\|\WERROR|\d{2}\W\d{2}\W\d{2},\d{3}\W\|\WWARNING',
    logs))
print('Ocorrência de Erros\n total de: ', len(erros), '\n')

hora = sorted(list(map(hora, erros)))

horas_unicas = sorted(list(set(hora)))

horas_unicas = {}
print(' Das  -  Até   -  Nº Erros')
for horario in hora:
    horas_unicas[horario] = hora.count(horario)

for horario_ord in sorted(horas_unicas, key=horas_unicas.get, reverse=True):
    print(horario + ':00 - ' + horario_ord + ':59', ' - ', horas_unicas[horario])