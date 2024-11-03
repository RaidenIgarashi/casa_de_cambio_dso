from controladores.controladorCliente import ControladorCliente
from controladores.controladorTroca import ControladorTroca
from controladores.controladorEmprestimo import ControladorEmprestimo
from controladores.controladorMoeda import ControladorMoeda
from telas.telaInicializador import TelaInicializador


class InicializadorSistema():
    def __init__(self):
        self.__tela_inicializador = TelaInicializador()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_moeda = ControladorMoeda(self) #ControladorMoeda(self)
        self.__controlador_troca = ControladorTroca(self, self.__controlador_moeda, self.__controlador_cliente)
        self.__controlador_emprestimo = None #ControladorEmprestimo(self)
       

    @property
    def tela_inicializadora(self):
        return self.__tela_inicializador
    
    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.cadastra_cliente, 2: self.cadastra_moeda, 3: self.cadastra_troca, 0:self.encerra_sistema}   

        encerrar = False
        while not encerrar:
            opcao_escolhida = self.__tela_inicializador.tela_opcoes()
            funcao_a_executar = opcoes[opcao_escolhida]
            funcao_a_executar()

    def encerra_sistema(self):
        print('***')
        print('Sistema desligando...')
        print('***')
        quit()

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()

    def cadastra_troca(self):
        self.__controlador_troca.abre_tela()

    def cadastra_emprestimo(self):
        self.__controlador_emprestimo.abre_tela()

    def cadastra_moeda(self):
        self.__controlador_moeda.abre_tela()
    
