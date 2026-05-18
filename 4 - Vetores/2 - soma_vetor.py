soma = 0
n = int(input('Quantos numeros voce vai digitar: '))
vetor = [0 for i in range(n)]
for i in range(0, n):
    vetor[i] = float(input('Digite um numero: '))
    soma += vetor[i]
    media = soma / n
print()

print('VALORES =', end='')
for i in range(0, n):
    print(f' {vetor[i]} ', end='')

print(f'\nSOMA = {soma}')
print(f'MEDIA = {media}')
