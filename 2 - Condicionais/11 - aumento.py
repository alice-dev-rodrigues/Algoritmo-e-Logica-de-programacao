perc = 0
salario = float(input('Digite o salario da pessoa: '))
if salario <= 1000:
    perc = salario * 20 / 100
    print(f'Novo salario = R${salario + perc}')
    print(f'Aumento = {perc}')
    print(f'Porcentagem = {20}%')

elif salario > 1000 and salario <= 3000:
    perc = salario * 15 / 100
    print(f'Novo salario = R${salario + perc}')
    print(f'Aumento = {perc}')
    print(f'Porcentagem {15}%')

elif salario > 3000 and salario <= 8000:
    perc = salario * 10 / 100
    print(f'Novo salario = {salario + perc}')
    print(f'Aumento = {perc}')
    print(f'Porcentagem = {10}%')
else:
    perc = salario * 5 / 100
    print(f'Novo salario = {salario + perc}')
    print(f'Aumento = {perc}')
    print(f'Porcentagem = {5}%')
    