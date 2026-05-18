duracao = 0
hi = int(input('Hora inicial: '))
hf = int(input('Hora final: '))
if hi > hf:
    duracao = (24 - hi) + hf
else:
    duracao = hf - hi
print(f'O JOGO DUROU {duracao} HORAS(S)')
