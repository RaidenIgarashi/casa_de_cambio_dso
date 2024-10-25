from abc import abstractmethod, ABC

class Controlador(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass

    @abstractmethod
    def mostra_dados(self):
        pass

    @abstractmethod
    def pega_objeto(self):
        pass

    @abstractmethod
    def inclui(self):
        pass

    @abstractmethod
    def exclui(self):
        pass

    @abstractmethod
    def altera(self):
        pass

    @abstractmethod
    def mostra_todas(self):
        pass
