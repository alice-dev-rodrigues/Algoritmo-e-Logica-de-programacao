n = int(input('Quantos numeros voce vai digitar? '))
vetor = [0 for x in range(n)]
for i in range(0, n):
    vetor[i] = int(input('Digite um numero: '))
for i in range(0, n):
    if vetor[i] < 0:
        print('NUMEROS NEGATIVOS:')
        print(vetor[i])