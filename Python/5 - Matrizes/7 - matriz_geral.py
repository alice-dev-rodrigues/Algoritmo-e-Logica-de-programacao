from time import sleep
n = int(input('Qual a ordem da matriz? '))

soma = 0
matriz = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):

        matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
        
# SOMA DOS POSITIVOS: 
        if matriz[i][j] > 0:
            soma += matriz[i][j]
print()
sleep(1)
print(f'SOMA DOS POSITIVOS: {soma}')
sleep(1)
print()

# LINHA ESCOLHIDA PARA IMPRIMIR
linha_escolhida = int(input('Escolha uma linha: '))
sleep(1)
print(f'LINHA ESCOLHIDA:', end=' ')
for i in range(0, n):
    for j in range(0, n):
        if i == linha_escolhida - 1:
            print(matriz[i][j], end=' ')
print()

# COLUNA ESCOLHIDA PARA IMPRIMIR
coluna_escolhida = int(input('\nEscolha uma coluna: '))
sleep(1)
print(f'COLUNA ESCOLHIDA:', end=' ')
for i in range(0, n):
    for j in range(0, n):
        if j == coluna_escolhida - 1:
            print(matriz[i][j], end=' ')
print()
sleep(1)

# DIAGONAL PRINCIPAL
print('\nDIAGONAL PRINCIPAL:', end=' ')
sleep(1)
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print(matriz[i][j], end=' ')
sleep(1)
print()

# MATRIZ ALTERADA
print('\nMATRIZ ALTERADA:')
sleep(1)
for i in range(0, n):
    for j in range(0, n):
        if matriz[i][j] < 0:
            matriz[i][j] = matriz[i][j] ** 2
        print(matriz[i][j], end=' ')
    print()
