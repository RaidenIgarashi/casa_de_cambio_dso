from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda
from DAOs.moeda_dao import MoedaDAO

class ControladorMoeda(Controlador):
    def __init__(self, controlador_sistema):
        self.__moeda_DAO = MoedaDAO()
        self.__tela = TelaMoeda()
        self.__controlador_sistema = controlador_sistema

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        if dados is not None:
            try:
                for moeda in self.__moeda_DAO.get_all():
                    if dados['nome'].lower() == moeda.nome.lower():
                        raise ValueError
            except:
                print()
                print(f'## a moeda {moeda.nome} já está registrada ##')
                print()
                return
            self.__moeda_DAO.add(Moeda(dados['nome'], dados['regioes'], dados['cifra'], dados['valor']))

    def exclui(self):
        nome = self.__tela.excluir()
        moeda = self.pega_objeto(nome)
        if moeda is not None:
            self.__moeda_DAO.remove(moeda.nome)
            self.__tela.mostrar_msg(f'A moeda {moeda.nome} foi excluida com sucesso')
        else:
            print()
            print('## Essa moeda não está registrada ##')
            print()

    def pega_objeto(self, nome):
        for moeda in self.__moeda_DAO.get_all():
            if nome.lower() == moeda.nome.lower():
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
        try:
            for moeda in self.__moeda_DAO.get_all():
                print('oi')
                self.__tela.mostrar_dados({'nome':moeda.nome, 'regioes':moeda.regioes, 'cifra':moeda.cifra, 'valor':moeda.valor_usd})
        except FileNotFoundError:
            self.__tela.mostrar_msg('## Não há moedas registradas ##')
            print()
    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {0: self.voltar_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.mostra_todas, 5: self.altera}
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  

    def mostra_dados(self):
        print('mostraDados')
        nome = self.__tela.ver_dados()
        for moeda in self.__moeda_DAO.get_all():
            if nome.lower() == moeda.nome.lower():
                self.__tela.mostrar_dados({'nome': moeda.nome, 'regioes': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd})
