class torcedor:
    def __init__(self, nome, idade, time):
        self.nome = nome
        self.idade = idade
        self.time = time
        
    def __str__(self):
        return f"Seu nome é {self.nome}, você tem {self.idade} anos e você torce pelo {self.time}"

p1 = torcedor("Matias", 54, "Náutico")
p2 = torcedor("Ana", 23, "Sport")
p3 = torcedor("Gabriel", '17', "Santa Cruz")

print(p1)
print(p2)
print(p3)