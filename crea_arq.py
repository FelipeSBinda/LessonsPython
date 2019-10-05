try:
    nome_arq = input('informe o nome do arquivo: ')
    arq = open(nome_arq, "a")

    nome = input('informe seu nome completo: ')
    arq.write(nome +'\n')
    arq.close()

except FileNotFoundError:
    print("arquivo não encontrado")
except FileExistsError:
    print('arquivo existente')