from programacao.controle.controlador_organizacao import ControladorOrganizacao
from programacao.limit.tela_inicializador import TelaInicializador

class Inicializador():
    def __init__(self):
        self.__tela = TelaInicializador()
        self.__org_controler = ControladorOrganizacao(self)

    @property
    def tela_inicializadora(self):
        return self.__tela
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_organizacao(self):
        self.__org_controler.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {2: self.cadastra_organizacao}

        while True:
            opcao_escolhida = self.__tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
