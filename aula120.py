

class Pessoa:
    nome = None
    idade = None
    def __init__(self, nome='Marcos', idade=42):
        self.nome = nome
        self.idade = idade
    
    
p1 = Pessoa('teste', 41)

print(p1.nome, p1.idade)
    