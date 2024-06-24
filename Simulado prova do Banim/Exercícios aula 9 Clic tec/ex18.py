# 18. O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente,
# deve ser maior que Min. Em seguida preencher a lista com todos os valores situados entre Min e Max que sejam
# divisíveis por 7. Exibir a lista resultante na tela.


Min = int(input("Digite o valor mínimo: "))
Max = int(input("Digite o valor máximo (maior que o mínimo): "))

# Verificando se Max é maior que Min
while Max <= Min:
    print("O valor máximo deve ser maior que o mínimo.")
    Max = int(input("Digite o valor máximo novamente: "))

# Preenchendo a lista com valores divisíveis por 7 entre Min e Max
lista = [num for num in range(Min, Max+1) if num % 7 == 0]

# Exibindo a lista resultante na tela
print("Lista resultante:", lista)