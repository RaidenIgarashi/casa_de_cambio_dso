from abc import abstractmethod, ABC

class Cliente(ABC):
    @abstractmethod
    def __init__(self, nome: str, id:str):
        self.__nome = nome 
        self.__id = id

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
