ordem = int(input('Qual a ordem da matriz? '))

matriz = [[0 for x in range(ordem)] for x in range(ordem)]
for i in range(0, ordem):
    for j in range(0, ordem):
        matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('MAIOR ELEMENTO DE CADA LINHA:')
for i in range(0, ordem):
    maior = 0
    for j in range(0, ordem):
        if j == 0:
            maior = matriz[i][j]
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(maior)