lista = []
for _ in range(5):
    n = int(input('Digite o número: '))
    # se a lista for vazia, insere
    inicio, fim = 0, len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if n < lista[meio]:
            fim = meio
        else:
            inicio = meio + 1
    lista.insert(inicio,n)
print(lista)