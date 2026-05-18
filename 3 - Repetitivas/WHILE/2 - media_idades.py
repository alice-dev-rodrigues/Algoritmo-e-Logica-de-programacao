soma = cont = 0
print('Digite as idades: ')
while True:
    
    idades = int(input(''))
    if cont == 0 and idades < 0:
        print('IMPOSSIVEL')
        break
    if idades < 0:
        print(f'MEDIA = {soma / cont:.2f}')
        break

    cont += 1
    soma += idades