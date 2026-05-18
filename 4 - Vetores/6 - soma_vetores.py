n = int(input('Quantos valores vai ter cada vetor? '))

vetorA = [0 for i in range(n)]
vetorB = [0 for i in range(n)]
vetorC = [0 for i in range(n)]

print('Digite os valores do vetor A:')
for i in range(0, n):
    vetorA[i] = int(input())

print('Digite os valores do vetor B:')
for i in range(0, n):
    vetorB[i] = int(input())

for i in range(0, n):
    vetorC[i] = vetorA[i] + vetorB[i]

print('VETOR RESULTANTE:')
for i in range(0, n):
    print(vetorC[i])
