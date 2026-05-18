n = int(input('Quantos elementos terá o vetor? '))
soma = 0
vetor = [0 for i in range(n)]

for i in range(0, n):
    vetor[i] = int(input('Digite um numero: '))
    if vetor[i] % 2 == 0:
        soma += vetor[i]
        media = soma / n

if any(n % 2 == 0 for n in vetor):
    print(f'MEDIA DOS PARES: {media}')
else:
    print('NENHUM NUMERO PAR')
