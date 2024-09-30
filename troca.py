from pessoa import Pessoa
from moeda import Moeda


class Troca:
    def __init__(self, id:int, pessoa:Pessoa, quantidade_usd:float, data:str, moeda_pedida:Moeda, moeda_entregue:Moeda, porcentagem_juros:int):
        self.__id = id
        self.__pessoa = pessoa
        self.__quantidade_usd = quantidade_usd
        self.__moeda_pedida = moeda_pedida
        self.__moeda_entregue = moeda_entregue
        self.__porcentagem_juros = porcentagem_juros

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def pessoa(self):
        return self.__pessoa
    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

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
    def porcentagem_juros(self):
        return self.__porcentagem_juros
    @porcentagem_juros.setter
    def porcentagem_juros(self, porcentagem_juros):
        self.__porcentagem_juros = porcentagem_juros

    def ver_troca(self):
        qnt = self.__quantidade_usd
        juros = self.__porcentagem_juros
        nome = self.__pessoa.nome
        data = self.__data
        m_ped = self.__moeda_pedida
        m_ent = self.__moeda_entregue
        print(f'Troca com valor de ${qnt} dólares feita por {nome}, no dia {data}. O cliente trocou 
              {m_ped.cifra}{qnt*m_ped.valor_usd} por {m_ent.cifra}{qnt*m_ent.valor_usd} com juros de {qnt * juros/100} dólares.')
