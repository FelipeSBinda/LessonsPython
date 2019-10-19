print("Bem vindo")

menu = '''1 - ler arquivo
2 - criar arquivo
3 - editar arquivo
4 - deletar arquivo
0 - sair\n'''

opnarq = 1
crearq = 2
editarq = 3
deletarq = 4
quitapp = 0
voltar = 9

print(menu)

opmenu = input("Escolha sua opção: ")


while opmenu != 0:
    if opnarq == 1:
        try:
            opnarq = input("Digite o nome do arquivo: ")
            arq = (opnarq, "r")
            print(arq.read())
            arq.close()
        except FileNotFoundError:
            print("arquivo não encontrado")
    elif crearq == 2:
        try:
            crearq = input("Digite o nome do arquivo")
            arq = open(crearq, "a")

            content = input('digite o conteudo: ')
            arq.write(content + '\n')
            arq.close()
        except FileExistsError:
            print('arquivo existente')
    elif editarq ==3:
        try:
            editarq = input('Informe o nome do arquivo: ')
            arq = open(editarq, "w")

            content = (input('Digite seu conteudo: '))
            arq.write(content + '/n')
            arq.close()
        except FileNotFoundError:
            print('Arquivo não encontrado')
    elif deletarq ==4:
        import os
        try:
            arq = deletarq = input('informe o nome do arquivo: ')
            os.remove(arq)

            print('arquivo excluído')

        except FileNotFoundError:
            print('arquivo inexistente')
    elif quitapp ==0:
        print("Obrigado por utilizar a aplicação!")