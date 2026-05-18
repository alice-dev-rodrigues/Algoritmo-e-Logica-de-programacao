n = int(input('Quantos alunos serão digitados? '))

vetornome = [0 for i in range(n)]
vetornota1 = [0 for i in range(n)]
vetornota2 = [0 for i in range(n)]

for i in range(0, n):
    print(f'Digite o nome, primeira e segunda nota do {i}o aluno')
    vetornome[i] = input('')
    vetornota1[i] = int(input())
    vetornota2[i] = int(input())
    
print('Alunos aprovados:')
for i in range(0, n):
    media = (vetornota1[i] + vetornota2[i]) / 2
    if media >= 6:
        print(vetornome[i])