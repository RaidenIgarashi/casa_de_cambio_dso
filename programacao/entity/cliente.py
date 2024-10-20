from abc import abstractmethod, ABC

class Cliente(ABC):
    @abstractmethod
    def __init__(self, nome: str, credito_usd: int):
        self.__nome = nome 
        # self.__identificacao = identificacao
        self.__credito_usd = credito_usd

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    # @property
    # def identificacao(self):
    #     return self.__identificacao

    # @identificacao.setter
    # def identificacao(self, identificacao):
    #     self.__identificacao = identificacao

    @property
    def credito_usd(self):
        return self.__credito_usd

    @credito_usd.setter
    def credito_usd(self, credito_usd):
        self.__credito_usd = credito_usd
