from abc import abstractmethod, ABC;

class Tela(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass

    @abstractmethod
    def pegar_dados(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def selecionar(self):
        pass

    @abstractmethod
    def mostra_msg(self, msg):
        print(msg)
