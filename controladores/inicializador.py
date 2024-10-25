from controladores.controladorCliente import ControladorCliente

from telas.telaInicializador import TelaInicializador

class Inicializador():
    def __init__(self):
        self.__tela = TelaInicializador()
        self.__controlador_cliente = ControladorCliente(self)

    @property
    def tela_inicializadora(self):
        return self.__tela
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_pessoa(self):
        self.__pessoa_controlador.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_cliente}

        while True:
            opcao_escolhida = self.__tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
