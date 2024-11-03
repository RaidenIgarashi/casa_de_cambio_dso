from entidades.pessoa import Pessoa
from entidades.moeda import Moeda


class Troca:
    def __init__(self, id:str, pessoa:Pessoa, quantidade_entrada:float, quantidade_saida:float, data:str, moeda_entrada:Moeda, moeda_saida:Moeda, porcentagem_juros:int):
        self.__id = id
        self.__pessoa = pessoa
        self.__quantidade_entrada = quantidade_entrada
        self.__quantidade_saida = quantidade_saida
        self.__moeda_entrada = moeda_entrada
        self.__moeda_saida = moeda_saida
        self.__porcentagem_juros = porcentagem_juros
        self.__data = data

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
    def quantidade_entrada(self):
        return self.__quantidade_entrada
    @quantidade_entrada.setter
    def quantidade_entrada(self, quantidade_entrada):
        self.__quantidade_entrada = quantidade_entrada

    @property
    def quantidade_saida(self):
        return self.__quantidade_saida
    @quantidade_saida.setter
    def quantidade_saida(self, quantidade_saida):
        self.__quantidade_saida = quantidade_saida

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def moeda_entrada(self):
        return self.__moeda_entrada
    @moeda_entrada.setter
    def moeda_entrada(self, moeda_entrada):
        self.__moeda_entrada = moeda_entrada

    @property
    def moeda_saida(self):
        return self.__moeda_saida
    @moeda_saida.setter
    def moeda_saida(self, moeda_saida):
        self.__moeda_saida = moeda_saida

    @property
    def porcentagem_juros(self):
        return self.__porcentagem_juros
    @porcentagem_juros.setter
    def porcentagem_juros(self, porcentagem_juros):
        self.__porcentagem_juros = porcentagem_juros

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    def ver_troca(self):
        qnt = self.__quantidade_usd
        juros = self.__porcentagem_juros
        nome = self.__pessoa.nome
        data = self.__data
        m_ped = self.__moeda_entrada
        m_ent = self.__moeda_saida
        print(f'Troca com valor de ${qnt} dólares feita por {nome}, no dia {data}. O cliente trocou \
              {m_ped.cifra}{qnt*m_ped.valor_usd} por {m_ent.cifra}{qnt*m_ent.valor_usd} com juros de {qnt * juros/100} dólares.')
