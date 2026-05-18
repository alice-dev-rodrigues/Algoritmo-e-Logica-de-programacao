n = int(input('Quantas pessoas serao digitadas? '))
soma = cont = menor = 0
nomedemenores = [0 for i in range(n + 1)]
nome = [0 for i in range(n + 1)]
idade = [0 for i in range(n + 1)]
altura = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    print(f'Dados da {i}a pessoa:')
    nome[i] = input('Nome: ')
    idade[i] = int(input('Idade: '))
    altura[i] = float(input('Altura: '))

    soma += altura[i]
    cont += 1

    if idade[i] < 16:
        menor += 1
        nomedemenores[i] = nome[i]

print(f'Altura média: {soma / cont:.2f}')
print(f'Pessoas com menos de 16 anos: {(menor / cont) * 100:.2f}%')
for i in range(1, n):
    print(nomedemenores[i])

