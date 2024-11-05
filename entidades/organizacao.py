from abstratas.absCliente import Cliente

class Organizacao(Cliente):
    def __init__(self, nome:str, id:str):
        super().__init__(nome, id)
        self.__emprestimos_pedidos = []
        self.__emprestimos_concedidos = []
