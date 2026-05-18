linhas = int(input('Qual a quantidade de linhas da matriz? '))
colunas = int(input('Qual a quantidade de colunas da matriz? '))

matriz = [[0 for x in range(colunas)] for i in range(linhas)]

print()
for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][i] = int(input(f'Elemento [{i},{j}]: '))

print()
print('VALORES NEGATIVOS:')
for i in range(0, linhas):
    for j in range(0, colunas):
        if matriz[i][j] < 0:
            print(matriz[i][j])
