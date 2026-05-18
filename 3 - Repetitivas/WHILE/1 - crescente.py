x = 0
y = 1
while x != y:
    print('Digite dois numeros:')
    x = int(input(''))
    y = int(input(''))
    if x < y:
        print('CRESCENTE!')
    elif x > y:
        print('DECRESCENTE!')
