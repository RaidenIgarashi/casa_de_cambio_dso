from abstratas.absCliente import Cliente
from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao
from entidades.moeda import Moeda
from entidades.devolucao import Devolucao


class Emprestimo:
    def __init__(self, id:int, cliente:Cliente, emprestador:Cliente, moeda:Moeda, quantia_repassada:float, data_do_repasse:str, 
                 data_pretendida: str, juros_normal:float, juros_mensal_atraso:float, devolvido:bool, data_devolvida: str):
        self.__id = id
        self.__cliente = cliente
        self.__emprestador = emprestador
        self.__moeda = moeda
        self.__quantia_repassada = quantia_repassada
        self.__data_do_repasse = data_do_repasse
        self.__data_devolvida = data_devolvida
        self.__data_pretendida = data_pretendida
        self.__juros_normal = juros_normal
        self.__juros_mensal_atraso = juros_mensal_atraso
        self.__devolvido = devolvido
        self.__devolucao = Devolucao(data_do_repasse, data_pretendida, juros_normal, juros_mensal_atraso, 
                                     devolvido, data_devolvida, quantia_repassada)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def emprestador(self):
        return self.__emprestador

    @emprestador.setter
    def emprestador(self, emprestador):
        self.__emprestador = emprestador

    @property
    def moeda(self):
        return self.__moeda

    @moeda.setter
    def moeda(self, moeda):
        self.__moeda = moeda

    @property
    def quantia_repassada(self):
        return self.__quantia_repassada

    @quantia_repassada.setter
    def quantia_repassada(self, quantia_repassada):
        self.__quantia_repassada = quantia_repassada

    @property
    def devolucao(self):
        return self.__devolucao

    @devolucao.setter
    def devolucao(self, devolucao):
        self.__devolucao = devolucao

    @property
    def data_do_repasse(self):
        return self.__data_do_repasse

    @data_do_repasse.setter
    def data_do_repasse(self, data_do_repasse):
        self.__data_do_repasse = data_do_repasse

    @property
    def data_devolvida(self):
        return self.__data_devolvida

    @data_devolvida.setter
    def data_devolvida(self, data_devolvida):
        self.__data_devolvida = data_devolvida

    @property
    def data_pretendida(self):
        return self.__data_pretendida

    @data_pretendida.setter
    def data_pretendida(self, data_pretendida):
        self.__data_pretendida = data_pretendida

    @property
    def juros_normal(self):
        return self.__juros_normal

    @juros_normal.setter
    def juros_normal(self, juros_normal):
        self.__juros_normal = juros_normal

    @property
    def juros_mensal_atraso(self):
        return self.__juros_mensal_atraso

    @juros_mensal_atraso.setter
    def juros_mensal_atraso(self, juros_mensal_atraso):
        self.__juros_mensal_atraso = juros_mensal_atraso

    @property
    def devolvido(self):
        return self.__devolvido

    @devolvido.setter
    def devolvido(self, devolvido):
        self.__devolvido = devolvido


