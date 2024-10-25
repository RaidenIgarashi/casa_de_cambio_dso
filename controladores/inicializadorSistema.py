from controladores.controladorCliente import ControladorCliente
from controladores.controladorTroca import ControladorTroca
from controladores.controladorEmprestimo import ControladorEmprestimo
from telas.telaInicializadora import TelaInicializadora

class InicializadorSistema():
    def __init__(self):
        self.__tela_inicializadora = TelaInicializadora()
        self.__controlador_cliente = ControladorCliente()
        self.__controlador_troca = ControladorTroca()
        self.__controlador_emprestimo = ControladorEmprestimo()

    @property
    def tela_inicializadora(self):
        return self.__tela_inicializadora
    
    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {0:self.encerra_sistema, 1: self.cadastra_cliente}   

        while True:
            opcao_escolhida = self.__tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def encerra_sistema(self):
        pass

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()

    def cadastra_troca(self):
        self.__controlador_troca.abre_tela()

    def cadastra_emprestimo(self):
        self.__controlador_emprestimo.abre_tela()
    
