n = int(input('Quantas pessoas voce vai digitar? '))
vetoridade = [0 for i in range(n + 1)]
vetornome = [0 for i in range(n + 1)]
maisvelho = 0
nomedomaisvelho = ''
for i in range(1, n + 1):
    print(f'Dados da {i}a pessoa')
    vetornome[i] = str(input('Nome: '))
    vetoridade[i] = int(input('Idade: '))

    if i == 0:
        maisvelho = vetoridade[i]
        nomedomaisvelho = vetornome[i]
    if vetoridade[i] > maisvelho:
        maisvelho = vetoridade[i]
        nomedomaisvelho = vetornome[i]


print(f'PESSOA MAIS VELHA: {nomedomaisvelho} ')