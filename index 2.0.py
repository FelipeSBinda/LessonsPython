def inputmenu():
    x = float(input("Digite o nome do arquivo:\n"))


def menu(x):
    opcao = int(input('''O que quer fazer com %x?
1 - ler arquivo
2 - criar arquivo
3 - editar arquivo
4 - deletar arquivo
0 - sair\n
Escolha:'''%(x)))
    if opcao == 1:
        try:
            opnarq = input("Digite o nome do arquivo: ")
            arq = (opnarq, "r")
            print(arq.read())
            arq.close()
        except FileNotFoundError:
            print("arquivo não encontrado")
    elif opcao == 2:
        try:
            crearq = input("Digite o nome do arquivo")
            arq = open(crearq, "a")

            content = input('digite o conteudo: ')
            arq.write(content + '\n')
            arq.close()
        except FileExistsError:
            print('arquivo existente')
    elif opcao ==3:
        try:
            editarq = input('Informe o nome do arquivo: ')
            arq = open(editarq, "w")

            content = (input('Digite seu conteudo: '))
            arq.write(content + '/n')
            arq.close()
        except FileNotFoundError:
            print('Arquivo não encontrado')
    elif opcao ==4:
        import os
        try:
            arq = input('informe o nome do arquivo: ')
            os.remove(arq)

            print('arquivo excluído')

        except FileNotFoundError:
            print('arquivo inexistente')
    elif opcao ==0:
        print("Obrigado por utilizar a aplicação!")
