a = 'A'
b = 'B'	
c =  1.1
formato = 'a={0}, b={1}, c={2:.2f}'.format(a, b, c)
print(formato)

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))
