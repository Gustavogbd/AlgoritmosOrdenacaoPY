minha_lista = []
troca = True #'Switch' para sair ou se manter no while
numero = int(input("Quantidade de números da sua Lista: "))

for i in range(numero): # Insere cada número da lista do usuário dentro da minha_lista
    valor = int(input("Insira os números da sua lista, um de cada vez: "))
    minha_lista.append(valor)

#Loop que implementa o Bubble Sort
while troca:
    troca = False
    for i in range(len(minha_lista) - 1):#Percorre os números da lista, e a cada iteração, compara com o número subsequente
        if minha_lista[i] > minha_lista[i + 1]:
            minha_lista [i], minha_lista[i + 1] = minha_lista[i+ 1], minha_lista[i] #Realiza a troca se o número selecionado for maior
            troca = True

print("Sua lista ordenada: ", minha_lista)
