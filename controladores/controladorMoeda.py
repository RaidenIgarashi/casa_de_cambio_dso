from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda

class ControladorMoeda(Controlador):
    def __init__(self, controlador_sistema):
        self.__moedas = [Moeda]
        self.__tela = TelaMoeda()
        self.__controlador_sistema = controlador_sistema
    
    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        self.__moedas.append(Moeda(dados['nome'], dados['regioes'], dados['cifra'], dados['valor']))

    def exclui(self):
        nome = self.__tela.selecionar()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            self.__moedas.remove(moeda)

    def pega_objeto(self, nome):
        for moeda in self.__moedas:
            if nome == moeda.nome:
                return moeda        

    def altera(self, nome):
        nome = self.__tela.selecionar()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            new_moeda = self.__tela.cadastrar_dados()
            moeda.nome = new_moeda['nome']
            moeda.regioes = new_moeda['reg']
            moeda.cifra = new_moeda['cifra']
            moeda.valor_usd = new_moeda['valor']

    def mostra_todas(self):
        for moeda in self.__moedas:
            self.__tela.mostrar({'nome':moeda.nome, 'reg':moeda.regioes, 'cifra':moeda.cifra, 'valor':moeda.valor})

    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        command_lst = {0: self.voltar_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.altera, 5: self.mostra_todas}
        while True:
            command_lst[self.__tela.tela_opcoes()]()

    def mostra_dados(self):
        nome = self.__tela.selecionar()
        for moeda in self.__moedas:
            if nome == moeda.nome:
                self.__tela.mostrar({'nome': moeda.nome, 'reg': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd})
