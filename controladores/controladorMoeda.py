from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda

class controladorMoeda(Controlador):
    def __init__(self):
        self.__moeda = [Moeda]
        self.__tela = TelaMoeda()
    
    def inclui(self):
        pass

    def exclui(self):
        pass

    def pega_objeto(self):
        pass

    def altera(self):
        pass

    def mostra_todas(self):
        pass

    def voltar_tela(self):
        pass

    def abre_tela(self):
        pass

    def mostra_dados(self):
        pass
