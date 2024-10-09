from entity.pessoa import Pessoa
from entity.organizacao import Organizacao
from entity.moeda import Moeda

class Emprestimo:
    def __init__(self, id:int, cliente:Pessoa, emprestador:Organizacao, quantidade_usd:float, data:str,
                 moeda_pedida:Moeda, moeda_entregue:Moeda, juros_mensal:int):
        if isinstance(cliente,Pessoa) and isinstance(emprestador, Organizacao):
            self.__cliente = cliente
            self.__emprestador = emprestador
        self.__id = id
        self.__quantidade_usd = quantidade_usd
        self.__data = data
        self.__moeda_pedida = moeda_pedida
        self.__moeda_entregue = moeda_entregue
        self.__juros_mensal = juros_mensal
        self.__emprestimo_pago = False

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
    def quantidade_usd(self):
        return self.__quantidade_usd

    @quantidade_usd.setter
    def quantidade_usd(self, quantidade_usd):
        self.__quantidade_usd = quantidade_usd

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def moeda_pedida(self):
        return self.__moeda_pedida

    @moeda_pedida.setter
    def moeda_pedida(self, moeda_pedida):
        self.__moeda_pedida = moeda_pedida

    @property
    def moeda_entregue(self):
        return self.__moeda_entregue

    @moeda_entregue.setter
    def moeda_entregue(self, moeda_entregue):
        self.__moeda_entregue = moeda_entregue

    @property
    def juros_mensal(self):
        return self.__juros_mensal

    @juros_mensal.setter
    def juros_mensal(self, juros_mensal):
        self.__juros_mensal = juros_mensal

    @property
    def emprestimo_pago(self):
        return self.__emprestimo_pago

    @emprestimo_pago.setter
    def emprestimo_pago(self, emprestimo_pago):
        self.__emprestimo_pago = emprestimo_pago




    def ver_estado_emprestimo(self, data_a_ver):
        qnt = self.quantidade_usd
        i = self.juros_mensal / 100
        nome = self.cliente.nome
        t = data_a_ver - self.data    #'t' precisa ser a quantidade de meses completos que passaram da data de empréstimo até a data pedida
        m_ped = self.moeda_pedida
        m_ent = self.moeda_entregue
        print(f"""Empréstimo com valor de ${qnt} dólares feito por {nome}, no dia {self.data}. O cliente pegou emprestado 
              {m_ped.cifra}{qnt*m_ped.valor_usd} e deve devolver {m_ent.cifra}{qnt*m_ent.valor_usd} com {i}% de juros mensal. 
              no dia {data_a_ver}, a quantidade a se pagar com juros cumulativo é de {qnt * (1 + i)**t}""")
