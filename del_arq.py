import os

try:
    nome_arq = input('informe o nome do arquivo: ')
    os.remove(nome_arq)

    print('arquivo excluído')

except FileNotFoundError:
    print('arquivo inexistente')