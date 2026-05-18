linhas = int(input('Quantas linhas tera a matriz? '))
colunas = int(input('Quantas colunas tera a matriz? '))

matriz = [[0 for i in range(colunas)] for i in range(linhas)]

for i in range(0, linhas):
    for j in range(0, colunas):
        matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(0, linhas):
    for j in range(0, colunas):
        print(matriz[i][j], end=' ')
    print()
