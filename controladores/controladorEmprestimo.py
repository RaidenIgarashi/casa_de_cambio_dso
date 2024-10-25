from telas.telaCliente import TelaCliente
from entidades.organizacao import Organizacao
from abstratas.absControlador import Controlador

class ControladorEmprestimo(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        
    def abre_tela(self):
        pass
