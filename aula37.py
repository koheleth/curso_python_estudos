

i = 0
numero = int(input('Digite um número: '))

while i < 100:
    i += 1
    if i % numero == 0:
        print(f'{i} é divisível por {numero}')
        continue
    print(i) # se não for divisível por 3, imprime o número normalmente