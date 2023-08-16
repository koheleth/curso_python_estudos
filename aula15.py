nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

ponto = (2, 3)
x = 2
y = 3
match ponto:
    case (0, 0):
        print('Origem')
    case (0, y):
        print(f'Eixo Y: {y}')
    case (x, 0):    
        print(f'Eixo X: {x}')
    case (x, y):
        print(f'Ponto: {x}, {y}')
        
        
