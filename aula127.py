import json

class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def to_json(self):
        return {
            'name': self.name,
            'age': self.age
        }

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

json_p1 = p1.to_json()
json_p2 = p2.to_json()

print(json_p1)
print(json_p2)

json_str = json.dumps(json_p1, indent=True)
print(json_str)
