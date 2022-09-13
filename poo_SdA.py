class SociedadeDoAnel:
    def __init__(self,nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def __portadordoanel(self):
        return 'Destrua o anel em Mordor'

    def getPortadordoanel(self,nome):
        if nome == 'Frodo':
            return self.__portadordoanel()
        else:
            return 'Você não é o portador'

sam = SociedadeDoAnel('Sam')
print(sam.getNome())
print(sam.getPortadordoanel('Sam'))

frodo = SociedadeDoAnel('Frodo')
print(frodo.getNome())
print(frodo.getPortadordoanel('Frodo'))