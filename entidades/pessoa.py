from abstratas.absCliente import Cliente


class Pessoa(Cliente):
    def __init__(self, nome:str, cpf:str, credito_usd:float, idade:int):
        super().__init__(nome, cpf, credito_usd)
        self.__idade = idade
        self.__emprestimos_pedidos = []
        self.__emprestimos_concedidos = []
        self.__trocas_feitas = []


    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
