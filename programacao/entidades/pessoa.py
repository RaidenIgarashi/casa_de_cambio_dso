from programacao.entidades.cliente import Cliente


class Pessoa(Cliente):
    def __init__(self, nome:str, cpf:str, idade:int, credito_usd:float):
        super().__init__(nome, credito_usd, cpf)
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




