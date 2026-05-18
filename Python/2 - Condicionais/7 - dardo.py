print('Digite as tres distancias:')

maior = 0
d1 = float(input(''))
d2 = float(input(''))
d3 = float(input(''))

if d1 > d2 and  d1 > d3:
    maior = d1
elif d2 > d1 and d2 > d3:
    maior = d2
elif d3 > d2 and d3 > d1:
    maior = d3
print(f'MAIOR DISTANCIA = {maior}')
