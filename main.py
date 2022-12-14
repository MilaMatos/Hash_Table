from hashpy import *
import platform
import os

tam = int(input("Insira o tamanho da tabela: "))
hash = [[] for _ in range(tam)]

print("Tabela vazia:")
exibir_hash(hash)

menu = 1
while menu == 1:
    if platform.system()=="Windows":
        os.system('cls')
    else: 
        print("\033c", end="")

    print("\n|Digite 1 para inserir uma nova chave |")
    print("|Digite 2 para remover uma chave      |")
    print("|Digite 3 para visualizar a tabela    |")
    print("|Qualquer valor diferente irá sair    |")
    opcao = int(input("\nOpção: "))
    if(opcao == 1):
        chave = int(input("Digite a chave: "))
        inserir(hash, chave)
    elif(opcao == 2):
        chave = int(input("Digite a chave: "))
        remover(hash, chave)
    elif(opcao == 3):
        exibir_hash(hash)
    else:
        menu = 0