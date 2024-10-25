from abstratas.absCliente import Cliente

class Organizacao(Cliente):
    def __init__(self, nome:str, cnpj:str, credito_usd:float):
        super().__init__(nome, cnpj, credito_usd)
        self.__emprestimos_pedidos = []
        self.__emprestimos_concedidos = []
