escala = input('Voce vai digitar a temperatura em qual escala (C/F)? ').upper()
temperatura = ''
if escala == 'C':
    temperatura = float(input('Digite a temperatura em Celsius: '))
    print(f'Temperatura equivalente em Fahrenheit: {(temperatura * 1.8) + 32:.2f}')
else:
    temperatura = float(input('Digite a temperatura em Fahrenheit: '))
    print(f'Temperatura equivalente em Celsius: {5 / 9 * (temperatura - 32):.2f}')
