from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda

class ControladorMoeda(Controlador):
    def __init__(self, controlador_sistema):
        self.__moeda = [Moeda]
        self.__tela = TelaMoeda()
        self.__controlador = controlador_sistema
    
    def inclui(self):
        dados_da_moeda = self.__tela.cadastrar_dados()
        self.__moeda.append(Moeda(dados_da_moeda['nome'], dados_da_moeda['reg'], dados_da_moeda['cifra'], dados_da_moeda['valor']))

    def exclui(self):
        nome = self.__tela.selecionar()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            self.__moeda.remove(moeda)

    def pega_objeto(self, nome):
        for moeda in self.__moeda:
            if nome == moeda.nome:
                return moeda
        self.__tela.mostra_msg('Moeda não existe')
        return

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
        for moeda in self.__moeda:
            self.__tela.mostrar({'nome':moeda.nome, 'reg':moeda.regioes, 'cifra':moeda.cifra, 'valor':moeda.valor})

    def voltar_tela(self):
        self.__controlador.abre_tela()

    def abre_tela(self):
        command_lst = {0: self.voltar_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.altera, 5: self.mostra_todas}
        continua = True
        while continua:
            command_lst[self.__tela.tela_opcoes()]()

    def mostra_dados(self):
        nome = self.__tela.selecionar()
        for moeda in self.__moeda:
            if nome == moeda.nome:
                self.__tela.mostrar({'nome': moeda.nome, 'reg': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd})
        return