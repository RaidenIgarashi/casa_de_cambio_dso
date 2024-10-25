from abstratas.absCliente import Cliente

class Organizacao(Cliente):
    def __init__(self, nome:str, cnpj:str, credito_usd:float):
        super().__init__(nome, credito_usd, cnpj)
        self.__emprestimos_pedidos = []
        self.__emprestimos_concedidos = []

