n = int(input('Quantos numeros voce vai digitar? '))
cont = 0
vetor = [0 for i in range(n)]

for i in range(0, n):
    vetor[i] = int(input('Digite um numero: '))

    if vetor[i] % 2 == 0:
        cont += 1
print()

print('NUMEROS PARES:')
for i in range(0, n):
    if vetor[i] % 2 == 0:
        print(vetor[i], end=' ')
print()
print(f'QUANTIDADE DE PARES = {cont}')