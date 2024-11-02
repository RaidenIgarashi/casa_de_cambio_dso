from abc import abstractmethod, ABC;

class Tela(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass

    @abstractmethod
    def cadastrar_dados(self):
        pass

    @abstractmethod
    def alterar_dados(self):
        pass

    @abstractmethod
    def mostrar_dados(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def ver_dados(self):
        pass

    @abstractmethod
    def mostrar_msg(self, msg):
        print(msg)
        print()
