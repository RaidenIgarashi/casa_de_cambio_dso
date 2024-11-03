from abstratas.absCliente import Cliente


class Pessoa(Cliente):
    def __init__(self, nome:str, cpf:str, credito_usd:float, idade:int):
        super().__init__(nome, cpf, credito_usd)
        self.__idade = idade
        self.__emprestimos_pedidos = []
        self.__emprestimos_concedidos = []
        self.__trocas_feitas = []
        self.__cpf = cpf


    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

