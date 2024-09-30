from pessoa import Pessoa
from organizacao import Organizacao
from moeda import Moeda

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




    def ver_estado_emprestimo(self, data):
        qnt = self.quantidade_usd
        juros = self.juros_mensal
        nome = self.cliente.nome
        t = data - self.data    #fazer com que 't' seja a quantidade de meses da data de empréstimo pra data pedida
        mped = self.moeda_pedida
        ment = self.moeda_entregue
        print(f'Empréstimo com valor de ${qnt} dólares feita por {nome}, no dia {data}. O cliente pegou emprestado \
              {mped.__cifra}{mped*mped.__valor_usd} e deve devolver {ment.cifra}{ment*ment.valor_usd} com {juros/100} de juros mensal. \
              nesta data, a quantidade a se pagar com juros cumulativo é de {qnt * (1 + (juros/100))**t}')
