largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
valordomq = float(input('Valor do metro quadrado: ')) 
area = largura * comprimento
print(f'Área do terreno = {area:.2f}')
print(f'Preço do terreno = {valordomq * area }')
