from math import sqrt
base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))
area = base * altura
perimetro = (2 * base) + (2 * altura)
hipotenusa = (base**2) + (altura**2)
print(f'AREA = {area:.4f}')
print(f'PERIMETRO = {perimetro:.4f}')
print(f'DIAGONAL = {sqrt(hipotenusa):.4f}')