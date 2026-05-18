while True:
    print('Digite os valores das coordenadas X e Y: ')
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print('QUADRANTE Q1')
    elif x < 0 and y > 0:
        print('QUADRANTE Q2')
    elif x < 0 and y < 0:
        print('QUADRANTE Q3')
    elif x > 0 and y < 0:
        print('QUADRANTE Q4')
    
    if x == 0 or y == 0:
        break
