try:
    print("Informe um número: ")
    n1 = int(input())
    print("Informe outro número: ")
    n2 = int(input())

    soma = n1 + n2
    print(soma)
    
except ValueError:
    print("Só digite números")
except:
    print("Algo de errado não está certo")
else:
    print("Agora foi")
