print("Gabriel Batista Rodrigues")
print("Pedro Rodrigues Ferreira")
print("Questão 2") 

N  = int(input('Digite um número: '))
while N < 6 or N > 32 or N % 2 != 0:
    print(f'O número {N} é inválido')
    N  = int(input('Digite um número: '))
print(' ','*' * (N-2),' ',sep='')
print('*' * N)
for c in range(N - 4):
    print("**", " " * (N-4), "**",sep='')
print('*' * N)
print(' ','*' * (N-2), ' ',sep='')
    
