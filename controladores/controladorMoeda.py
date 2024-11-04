from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda

class ControladorMoeda(Controlador):
    def __init__(self, controlador_sistema):
        self.__moedas = [Moeda('Dólar', ['EUA', 'Canada'], '$', 1), Moeda('Real', ['Brasil'], 'R$', 5.70)]
        self.__tela = TelaMoeda()
        self.__controlador_sistema = controlador_sistema

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        try:
            for moeda in self.__moedas:
                if dados['nome'] == moeda.nome:
                    raise ValueError
        except:
            print()
            print(f'## a moeda {moeda.nome} já está registrada ##')
            print()
        self.__moedas.append(Moeda(dados['nome'], dados['regioes'], dados['cifra'], dados['valor']))

    def exclui(self):
        nome = self.__tela.excluir()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            self.__moedas.remove(moeda)
            self.__tela.mostrar_msg(f'A moeda {moeda.nome} foi excluida com sucesso')
        else:
            print()
            print('## Essa moeda não está registrada ##')
            print()

    def pega_objeto(self, nome):
        for moeda in self.__moedas:
            if nome == moeda.nome:
                return moeda        

    def altera(self):
        nome = self.__tela.alterar_dados()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            new_moeda = self.__tela.cadastrar_dados()
            moeda.nome = new_moeda['nome']
            moeda.regioes = new_moeda['regioes']
            moeda.cifra = new_moeda['cifra']
            moeda.valor_usd = new_moeda['valor']
        else:
            print()
            print('## Essa moeda não está registrada ##')
            print()
            
    def mostra_todas(self):
        if self.__moedas == []:
            self.__tela.mostrar_msg('## Não há moedas registradas ##')
            print()
        for moeda in self.__moedas:
            self.__tela.mostrar_dados({'nome':moeda.nome, 'regioes':moeda.regioes, 'cifra':moeda.cifra, 'valor':moeda.valor_usd})

    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        command_lst = {0: self.voltar_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.mostra_todas, 5: self.altera}
        while True:
            command_lst[self.__tela.tela_opcoes()]()

    def mostra_dados(self):
        nome = self.__tela.ver_dados()
        for moeda in self.__moedas:
            if nome == moeda.nome:
                self.__tela.mostrar_dados({'nome': moeda.nome, 'regioes': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd})
