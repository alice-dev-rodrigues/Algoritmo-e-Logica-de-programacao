n = int(input('Qual a ordem da matriz? '))

matriz = [[0 for x in range(n)] for x in range(n)]
vetornegativos = [0 for i in range(10)]
contador = 0

for i in range(0, n):
    for j in range(0, n):
        matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
        if matriz[i][j] < 0:
            contador += 1

print()
print('DIAGONAL PRINCIPAL:')
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print(matriz[i][j], end=' ')

print(f'\nQUANTIDADE DE NEGATIVOS = {contador}')   
