class Organizacao:
    def __init__(self, nome:str, cnpj:str, credito_usd:float):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__emprestimos_pedidos = []
        self.__emprestimos_cedidos = []
        self.__credito_usd = credito_usd

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def credito_usd(self):
        return self.__credito_usd

    @credito_usd.setter
    def credito_usd(self, credito_usd):
        self.__credito_usd = credito_usd

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

