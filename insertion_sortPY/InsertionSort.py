lista = []
numero = int(input("Quantidade de números da sua Lista: "))

for i in range(numero): # Insere cada número da lista do usuário dentro da minha_lista
    valor = int(input("Insira os números da sua lista, um de cada vez: "))
    lista.append(valor)

def insertionSort(lista):
    n = len(lista)

    for i in range(1, n):
        chave = lista[i] #2
        j = i - 1 #13

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave

insertionSort(lista)

print("Sua lista ordenada: ", lista)