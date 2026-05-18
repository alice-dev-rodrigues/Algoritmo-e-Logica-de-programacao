print('Digite dois numeros inteiros: ')
x = int(input())
y = int(input())
soma = 0
if y < x:
    for i in range(y, x + 1):
        if i % 2 != 1:
            soma += i
else:
    for i in range(x, y + 1):
        if i % 2 != 1:
            soma += i
print(soma)
