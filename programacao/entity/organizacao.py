from programacao.entity.cliente import Cliente

class Organizacao(Cliente):
    def __init__(self, nome:str, cnpj:str, credito_usd:float):
        super().__init__(nome, credito_usd)
        self.__cnpj = cnpj
        self.__emprestimos_pedidos = []
        self.__emprestimos_cedidos = []

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

#o tipo_pedido é um bool que serva para identificar se é um emprestimo do tipo pedido ou cedido
    def add_emprestimo(self, emprestimo, tipo_pedido:bool):
            if tipo_pedido:
                for emp_pedido in self.__emprestimos_pedidos:
                    if emp_pedido.id == emprestimo.id:
                        print(f'O emprestimo {emprestimo.id} ja está cadastrado')
                        return None
                self.__emprestimos_pedidos.append(emprestimo)
            elif not tipo_pedido:
                for emp_cedido in self.__emprestimos_cedidos:
                    if emp_cedido.id == emprestimo.id:
                        print(f'O emprestimo {emprestimo.id} ja está cadastrado')
                        return None
                self.__emprestimos_cedidos.append(emprestimo)
            else:
                print('emprestimo não foi entregue corretamente')
