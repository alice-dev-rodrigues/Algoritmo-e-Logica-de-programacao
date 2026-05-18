linhas = int(input('Quantas linhas terá cada matriz? '))
colunas = int(input('Quantas colunas terá cada matriz? '))

matrizA = matrizB = matrizC = [[0 for x in range(colunas)] for x in range(linhas)]

print('Digite os valores da matriz A')
for i in range(0, linhas):
    for j in range(0, colunas):
        matrizA[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('Digite os valores da matriz B')
for i in range(0, linhas):
    for j in range(0, colunas):
        matrizB[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('Matriz soma:')
for i in range(0, linhas):
    for j in range(0, colunas):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
        print(matrizC[i][j], end=' ')
    print()
