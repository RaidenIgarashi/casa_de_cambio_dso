from controladores.controladorCliente import ControladorCliente
from controladores.controladorTroca import ControladorTroca
from controladores.controladorEmprestimo import ControladorEmprestimo
from controladores.controladorMoeda import ControladorMoeda
from controladores.relatorio import Relatorio
from telas.telaInicializador import TelaInicializador


class InicializadorSistema():
    def __init__(self):
        self.__relatorio = Relatorio()
        self.__tela_inicializador = TelaInicializador()
        self.__controlador_cliente = ControladorCliente(self, self.__relatorio)
        self.__controlador_moeda = ControladorMoeda(self, self.__relatorio) 
        self.__controlador_troca = ControladorTroca(self, self.__controlador_moeda, self.__controlador_cliente, self.__relatorio)
        self.__controlador_emprestimo = ControladorEmprestimo(self, self.__controlador_moeda, self.__controlador_cliente, self.__relatorio)
       

    @property
    def tela_inicializadora(self):
        return self.__tela_inicializador
    
    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.cadastra_cliente, 2: self.cadastra_moeda, 3: self.cadastra_troca, 
                  4: self.cadastra_emprestimo, 5: self.gera_relatorio, 0:self.encerra_sistema}   

        while True:
            opcao_escolhida = self.__tela_inicializador.tela_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  

    def encerra_sistema(self):
        quit()

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()

    def cadastra_troca(self):
        self.__controlador_troca.abre_tela()

    def cadastra_emprestimo(self):
        self.__controlador_emprestimo.abre_tela()

    def cadastra_moeda(self):
        self.__controlador_moeda.abre_tela()
    
    def gera_relatorio(self):
        self.__relatorio.gera_relatorio()
