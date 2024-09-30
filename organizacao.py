#rom emprestimo import Emprestimo
from troca import Troca


class Organizacao:
    def __init__(self, nome:str, cnpj:str, credito_usd:float):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__emprestimos_pedidos = []
        self.__emprestimos_cedidos = []
        self.__credito_usd = credito_usd
