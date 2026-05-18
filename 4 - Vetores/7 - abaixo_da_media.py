n = int(input('Quantos elementos terá o vetor? '))
soma = 0

vetor = [0 for i in range(n)]

for i in range(0, n):
    vetor[i] = float(input('Digite um numero: '))
    soma += vetor[i]
    media = soma / n

print(f'MEDIA DO VETOR = {media:.3f}')
print('ELEMENTOS ABAIXO DA MEDIA:')
for i in range(0, n):
    if media > vetor[i]:
        print(vetor[i])
