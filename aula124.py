from datetime import datetime

class Pessoa:
    atributo= 'valor'
    def __init__(self, nome='Marcos', idade=35):
        self.idade = idade
        self.nome = nome
        
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    def get_ano_nascimento(self):
        return datetime.now().year - self.idade
    
    
p1 = Pessoa(nome='Luciano', idade=40)
p2 = Pessoa(nome='Marcos', idade=43)
dados = {'idade': 36, 'nome': 'Aurelio'}
p3 = Pessoa(**dados)


print(p1.get_ano_nascimento())
print(Pessoa.get_ano_nascimento(p2))
print(p1.__dict__)
print(p2.__dict__)
print(vars(p1))
print(vars(p2))
print(vars(p3))

