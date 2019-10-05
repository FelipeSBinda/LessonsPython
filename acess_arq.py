try:
    nome_arq = input('Informe o nome do arquivo: ')
    arq = open(nome_arq, "r")
    '''for i in arq:
        print(i)'''
    print(arq.read())
    arq.close()

    '''print(arq.read())
    print(arq.readline())'''

except FileNotFoundError:
    print('Arquivo não encontrado')


""""
'r' - read. valor: default
abre um arquivo para leitura
caso o arquivo não exista, um erro é reportado
'a' - append
abre o arquivo em modo edição
se o arquivo não existir, o mesmo é criado
preservando o conteudo atual, adicionando a alteração ao final do produto
'w' - write
abre o arquivo para edição
cria o arquivo se o mesmo não existir
substitui o conteudo atual pelo novo
'x' - create
cria um arquivo com nome informado, e caso já exista, um erro é reportado
"""