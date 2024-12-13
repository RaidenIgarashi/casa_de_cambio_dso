from abstratas.absCliente import Cliente


class Pessoa(Cliente):
    def __init__(self, nome:str, id:str, idade:int):
        super().__init__(nome, id)
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def trocas_feitas(self):
        return self.__trocas_feitas

    @trocas_feitas.setter
    def trocas_feitas(self, trocas):
        self.__trocas_feitas.append(trocas)

    @property
    def emprestimos_pedidos(self):
        return self.__emprestimos_pedidos

    @emprestimos_pedidos.setter
    def emprestimos_pedidos(self, emprestimo):
        self.__emprestimos_pedidos.append(emprestimo)

    def emprestimos_pedidos_remove(self, emprestimo):
        self.__emprestimos_pedidos.remove(emprestimo)

    @property
    def emprestimos_concedidos(self):
        return self.__emprestimos_concedidos

    @emprestimos_concedidos.setter
    def emprestimos_concedidos(self, emprestimo):
        self.__emprestimos_concedidos.append(emprestimo)

    def emprestimos_concedidos_remove(self, emprestimo):
        self.__emprestimos_concedidos.remove(emprestimo)