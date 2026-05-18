alcool = gasolina = diesel = 0
codigo = 0
while True:
    codigo = int(input('Informe um codigo (1, 2, 3) ou 4 para parar: '))
    
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break

print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')