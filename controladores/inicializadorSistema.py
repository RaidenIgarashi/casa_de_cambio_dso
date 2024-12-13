from controladores.controladorCliente import ControladorCliente
from controladores.controladorTroca import ControladorTroca
from controladores.controladorEmprestimo import ControladorEmprestimo
from controladores.controladorMoeda import ControladorMoeda
from controladores.controladorRelatorio import Relatorio
from telas.telaInicializador import TelaInicializador


class InicializadorSistema():
    def __init__(self):
        self.__tela_inicializador = TelaInicializador()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_moeda = ControladorMoeda(self) 
        self.__controlador_troca = ControladorTroca(self, self.__controlador_moeda, self.__controlador_cliente)
        self.__controlador_emprestimo = ControladorEmprestimo(self, self.__controlador_moeda, self.__controlador_cliente)
        self.__inclusoes = []
        self.__alteracoes = []
        self.__exclusoes = []
        self.__mostragens = []
        self.__indefinidos = []
        self.__relatorio = Relatorio(self, self.__controlador_cliente, self.__controlador_moeda, self.__controlador_troca, self.__controlador_emprestimo)
        
    
    def add_operacao(self, tipo: str, info: str):
        if tipo == 'inclusao':
            self.__inclusoes.append(info)
        elif tipo == 'alteracao':
            self.__alteracoes.append(info)
        elif tipo == 'exclusao':
            self.__exclusoes.append(info)
        elif tipo == 'mostragem':
            self.__mostragens.append(info)
        else:
            self.__indefinidos.append(info)
    @property
    def inclusoes(self):
        return self.__inclusoes
    @property
    def alteracoes(self):
        return self.__alteracoes
    @property
    def exclusoes(self):
        return self.__exclusoes
    @property
    def mostragens(self):
        return self.__mostragens
    @property
    def indefinidos(self):
        return self.__indefinidos

    @property
    def tela_inicializadora(self):
        return self.__tela_inicializador
    
    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.cadastra_cliente, 2: self.cadastra_moeda, 3: self.cadastra_troca, 
                  4: self.cadastra_emprestimo, 5: self.gera_relatorio, 6:self.relatorio_acoes_usuario, 0:self.encerra_sistema}   

        while True:
            opcao_escolhida = self.__tela_inicializador.init_opcoes()
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
        
    def relatorio_acoes_usuario(self):
        self.__relatorio.relatorio_acoes_usuario()
