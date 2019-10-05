try:
    arq = nome_arq = input('Informe o nome do arquivo: ')
    arq = open(nome_arq, "a")

    '''para editar um arquivo'''
    nome = (input('Informe seu nome completo: '))
    arq.write(nome + '/n')
    arq.close()

    arq = open(nome_arq, "r")
    print(arq.read())

    arq.close()
except FileNotFoundError:
    print('Arquivo não encontrado')