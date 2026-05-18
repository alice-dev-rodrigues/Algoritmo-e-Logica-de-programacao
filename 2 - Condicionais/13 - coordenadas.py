x = float(input('Valor de x: '))
y = float(input('Valor de y: '))
if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y == 0:
    print('ORIGEM')
elif x == 0 and y > 0 or y < 0:
    print('EIXO Y')
elif y == 0 and x > 0 or x < 0:
    print('EIXO X')
