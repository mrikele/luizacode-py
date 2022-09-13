class Hobbit:
    def __init__(self,nome,especie,comida_fav):
        self.nome = nome
        self.especie = especie
        self.comida_fav = comida_fav

    def getNome(self):
        return f'Esse hobbit se chama {self.nome}'
    
    def getComida(self):
        return f'Esse hobbit adora comer {self.comida_fav} no segundo café da manhã'

    def getEspecie(self):
        return f'A espécie desse hobbit é {self.especie}'

class Frodo(Hobbit):
    def __init__(self,nome,especie,comida_fav,sobrenome):
        self.sobrenome = sobrenome
        super().__init__(nome,especie,comida_fav)

    def getSobrenome(self):
        return f'O sobrenome do Frodo é {self.sobrenome}'


frodo = Frodo('Frodo', 'Pés Peludos', 'Batatas', 'Bolseiro')
print(frodo.getSobrenome())