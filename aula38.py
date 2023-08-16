qtd_linhas = 5
qtd_colunas = 5


linha = 1
print(65*'-')
while linha <= qtd_linhas:
    coluna = 1
    print(f'| {linha=}', end="")
    while coluna <= qtd_colunas:
        coluna += 1
        if linha == 1:
            print(f'|  {coluna=}', end="")
        else:
            print(f'| {len("coluna=  ")*" "}', end="")
        
    print('|')
    print(65*'-')
    linha += 1
    