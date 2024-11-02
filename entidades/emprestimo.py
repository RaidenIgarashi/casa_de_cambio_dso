from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao
from entidades.moeda import Moeda
from entidades.devolucao import Devolucao
from datetime import date

class Emprestimo:
    def __init__(self, id:int, cliente:Pessoa, emprestador:Organizacao, moeda:Moeda, quantia_repassada:float, data_do_repasse:date, 
                 data_pretendida:date, juros_normal:float, juros_mensal_atraso:float, devolvido:bool, data_devolvida:date):
        
        if isinstance(cliente, Pessoa) and isinstance(emprestador, Organizacao):
            self.__id = id
            self.__cliente = cliente
            self.__emprestador = emprestador
            self.__moeda = moeda
            self.__quantia_repassada = quantia_repassada
            self.__devolucao = Devolucao(data_do_repasse, data_pretendida, juros_normal, juros_mensal_atraso, devolvido, data_devolvida, quantia_repassada)

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
