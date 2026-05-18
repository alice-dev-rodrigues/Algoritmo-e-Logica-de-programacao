dentro = fora = 0
quant = int(input('Quantos numeros voce vai digitar? '))
for i in range(0, quant):
    n = int(input('Digite um numero: '))
    if n >= 10 and n <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} DENTRO')
print(f'{fora} FORA')
