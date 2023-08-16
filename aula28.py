nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    idade = int(idade)
    if idade >= 18:
        print(f'{nome} é maior de idade')
    else:
        print(f'{nome} é menor de idade')
        
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
        
    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')    
else:
    print('Você não digitou os dados corretamente')        
