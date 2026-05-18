linhas = int(input('Qual é a quantidade de linhas da matriz? '))
colunas = int(input('Qual é a quantidade de colunas da matriz? '))

matriz = [[0 for x in range(colunas)] for x in range(linhas)]
vetor = [0 for i in range(linhas)]

for i in range(0, linhas):
    soma = 0
    print(f'Digite os elementos da {i + 1}a linha')
    for j in range(0, colunas):
        matriz[i][j] = float(input())
        soma += matriz[i][j]
        vetor[i] = soma

print('VETOR GERADO:')
for i in range(0, linhas):
    print(vetor[i]) 
    