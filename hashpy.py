#Tabela de dispersão de encadeamento externo

def hashing(hash, chave):
    return chave % len(hash)
  
def inserir(hash, chave):
    indice = hashing(hash, chave)
    hash[indice].append(chave)

def aux_busca(hash, chave):
    indice = hashing(hash, chave)
    i=0

    while (i != len(hash[indice])):
        if hash[indice][i] == chave:
            return i
        i = i+1

    if i == len(hash[indice]):
            return -1

def busca(hash, chave):
    indice = hashing(hash, chave)
    pos = aux_busca(hash, chave)
    if pos == -1:
        print("Não foi encontrado")
        return pos
    return hash[indice][pos]

def remover(hash, chave):
    indice = hashing(hash, chave)
    i = aux_busca(hash, chave)
    if i == -1:
        print("\nChave não existe")
        input("Pressione ENTER para continuar")
    else:
        hash[indice].pop(i)
        print("\nChave removida com sucesso")
        input("Pressione ENTER para continuar")

def exibir_hash(hashTable):
    print("\n")
      
    for i in range(len(hashTable)):
        print(i,"|", end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
    print("\n")
    input("\nPressione ENTER para continuar")


