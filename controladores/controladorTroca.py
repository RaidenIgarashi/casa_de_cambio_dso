from telas.telaTroca import TelaTroca
from abstratas.absControlador import Controlador

class ControladorTroca(Controlador):
    def __init__(self, controlador_sistema):
        self.__trocas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaTroca()

    def abre_tela(self):
        pass