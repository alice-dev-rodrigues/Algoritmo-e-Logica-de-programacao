duração = int(input('Digite a duração em segundos: '))
horas = duração // 3600
minutos = (duração % 3600) // 60
segundos = duração % 60
print(f'{horas}:{minutos}:{segundos}')
