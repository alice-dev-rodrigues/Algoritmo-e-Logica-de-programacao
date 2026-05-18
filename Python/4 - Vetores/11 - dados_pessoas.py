n = int(input('Quantas pessoas serao digitadas? '))

menoraltura = maioraltura = contador_altura = contador = soma = 0
vetoraltura = [0 for i in range(n + 1)]
vetorgenero = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    vetoraltura[i] = float(input(f'Altura da {i}a pessoa: '))
    vetorgenero[i] = input(f'Genero da {i} pessoa: ').upper()

# MENOR E MAIOR ALTURA
    if i == 0:
        menoraltura = vetoraltura[i]
        maioraltura = vetoraltura[i]
    if vetoraltura[i] < menoraltura:
        menoraltura = vetoraltura[i]
    elif vetoraltura[i] > maioraltura:
        maioraltura = vetoraltura[i]    

# MEDIA DAS ALTURAS DAS MULHERES
    if vetorgenero[i] == 'F':
        contador_altura += 1
        soma += vetoraltura[i]
        media = soma / contador_altura

# NUMERO DE HOMENS
    if vetorgenero[i] == 'M':
        contador += 1

print(f'Menor altura = {menoraltura}')
print(f'Maior altura = {maioraltura}')
print(f'Média das alturas das mulheres = {media:.2f}')
print(f'Numero de homens = {contador}')
