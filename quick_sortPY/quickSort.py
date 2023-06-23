#Versão simplificada usando as característica do Python
def quickSort(dados):
  if len(dados) < 2:
    return dados
  else:
    pivot = dados[0]
    menores = [i for i in dados[1:] if i <= pivot]
    maiores = [i for i in dados[1:] if i >  pivot]
    return quickSort(menores) + [pivot] + quickSort(maiores)


#Programa Principal
dados = [50, 25, 92, 16, 76, 30, 43, 54, 19]
dados = quickSort(dados)
print(dados)