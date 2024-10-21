from  programacao.entity.emprestimo import Emprestimo
from  programacao.entity.troca import Troca
from programacao.entity.cliente import Cliente


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

    @property
    def emprestimos_pedidos(self):
        return self.__emprestimos_pedidos
    
    def add_emprestimo(self, emp:Emprestimo):
        if emp.cliente == self and emp not in self.__emprestimos_pedidos:
            self.__emprestimos_pedidos.append(emp)
        elif emp.emprestador == self and emp not in self.__emprestimos_concedidos:
            self.__emprestimos_concedidos.append(emp)
        self.atualizar_credito()

    def del_emprestimo(self, emp:Emprestimo):
        if emp in self.__emprestimos_pedidos:
            self.__emprestimos_pedidos.remove(emp)
        elif emp in self.__emprestimos_concedidos:
            self.__emprestimos_concedidos.remove(emp)
        self.atualizar_credito()

    def atualizar_credito(self):
        pos, neg = 0, 0
        for emp in self.__emprestimos_concedidos:
            pos += emp.quantidade_usd
        for emp in self.__emprestimos_pedidos:
            neg += emp.quantidade_usd
        self.credito_usd = pos - neg

    @property
    def trocas_feitas(self):
        return self.__trocas_feitas
    
    def add_troca(self, troca:Troca):
        if troca.pessoa == self and troca not in self.__trocas_feitas:
            self.__trocas_feitas.append(troca)

    def del_troca(self, troca:Troca):
        if troca in self.__trocas_feitas:
            self.__trocas_feitas.remove(troca)

    @property
    def credito_usd(self):
        return self.__credito_usd
    @credito_usd.setter
    def credito_usd(self, credito_usd):
        self.__credito_usd = credito_usd
