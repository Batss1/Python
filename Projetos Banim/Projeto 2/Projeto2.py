print("\nGerador de Senhas")
print("\nPor:\nCaio Luiz Argentino Firmino")
print("Gabriel Batista Rodrigues")
print("Pedro Côrtes Loureiro\n------------------------")

#Importando a função choice da biblioteca random
from random import choice
#Leitura das matriculas e gravação na lista dados
arq = open('MATR.txt','r',encoding='utf-8')
s = arq.readline().rstrip()
dados = []
while s != '':
    dados.append(s)
    s = arq.readline().rstrip()
arq.close()

#Função que gera as senhas a partir do Tipo digitado e do Tamanho
def GeraSenha(Tipo, Tam):  
    senha = ''
    match Tipo:
        case 'a': 
            lista = [chr(i) for i in range(48,58)]
        
        case 'b':
            lista = [chr(i) for i in range(65,91)] 
            lista += [chr(c) for c in range(97,123)]
        
        case 'c':
            lista = [chr(i) for i in range(65,91)] 
            lista += [chr(i) for i in range(48,58)]
        
        case 'd':
            lista = [chr(i) for i in range(65,91)] 
            lista += [chr(c) for c in range(97,123)]
            lista += [chr(i) for i in range(48,58)]
        
        case 'e':
            lista = [chr(i) for i in range(65,91)] 
            lista += [chr(c) for c in range(97,123)]
            lista += [chr(i) for i in range(48,58)]
            lista += ["-", "_", ":", "@", "#", "$", "&", "?"]
    
    for _ in range(Tam):
        senha += choice(lista)
    return senha

#Input do tipo de senhas geradas
Tipo = input('''Tipos de senhas -
a. Numérica – conterá apenas algarismos;
b. Alfabética – conterá apenas letras maiúsculas e minúsculas;
c. Alfanumérica 1 – conterá letras maiúsculas e algarismos;
d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;
e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres "-", "_", ":", "@", "#", "$", "&", "?"

Digite o tipo de senha que quer gerar: ''').lower().strip()

#Input do tamanho das senhas que vão ser geradas
Tam = int(input('\nDigite o tamanho da senha: '))

#Gravação das senhas geradas com a função em SENHAS.txt
num = 0
saida = open('SENHAS.txt', 'w')
while num < len(dados):
    saida.write(f'{dados[num]}; {GeraSenha(Tipo,Tam)};\n')
    num += 1
saida.close()
print('\nSenhas geradas com sucesso\nFim do Programa')