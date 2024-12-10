from abc import abstractmethod, ABC;

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
        
    @abstractmethod
    def mostrar_msg(self, msg):
        pass
    
    @abstractmethod
    def open(self):
        botao, valores = self.__window.Read()
        return botao, valores

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
    def mostrar_tabela(self):
        pass

    @abstractmethod
    def excluir(self):
        pass

    @abstractmethod
    def ver_dados(self):
        pass

    
