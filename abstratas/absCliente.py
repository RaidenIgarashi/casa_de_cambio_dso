from abc import abstractmethod, ABC

class Cliente(ABC):
    @abstractmethod
    def __init__(self, nome: str, id:str, credito_usd: int):
        self.__nome = nome 
        self.__id = id
        self.__credito_usd = credito_usd

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def credito_usd(self):
        return self.__credito_usd

    @credito_usd.setter
    def credito_usd(self, credito_usd):
        self.__credito_usd = credito_usd
