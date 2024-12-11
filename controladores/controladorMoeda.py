from abstratas.absControlador import Controlador
from entidades.moeda import Moeda
from telas.telaMoeda import TelaMoeda
from DAOs.moeda_dao import MoedaDAO
from datetime import datetime as dt
from excecoes import *

class ControladorMoeda(Controlador):
    def __init__(self, controlador_sistema, relatorio):
        self.__moeda_DAO = MoedaDAO()
        self.__tela = TelaMoeda()
        self.__controlador_sistema = controlador_sistema
        self.__relatorio = relatorio
        
    def abre_tela(self):
        opcoes = {1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.mostra_todas, 5: self.altera, 0: self.voltar_tela}
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        if dados is not None:
            try:
                for moeda in self.__moeda_DAO.get_all():
                    if dados['nome'].lower() == moeda.nome.lower():
                        ValueError
            except:
                self.__tela.mostrar_msg(f'\n## a moeda {moeda.nome} já está registrada ##\n')
                return
            self.__moeda_DAO.add(Moeda(dados['nome'], dados['regioes'], dados['cifra'], dados['valor']))
            self.__tela.mostrar_msg(f'Moeda {dados['nome']} adicionada com sucesso')
            self.__relatorio.add_operacao('inclusao', f"Inclusao da Moeda '{dados['nome']}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            

    def exclui(self):
        nome = self.__tela.excluir()
        if nome != None:
            moeda = self.pega_objeto(nome)
            if moeda != None:
                self.__moeda_DAO.remove(moeda.nome)
                self.__tela.mostrar_msg(f'A moeda {moeda.nome} foi excluida com sucesso')
                self.__relatorio.add_operacao('exclusao', f"Exclusao da Moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                MoedaNaoEncontrada

    def pega_objeto(self, nome):
        if nome != None:
            for moeda in self.__moeda_DAO.get_all():
                if nome.lower() == moeda.nome.lower():
                    return moeda     
            return None   

    def altera(self):
        nome = self.__tela.alterar_dados()
        if nome != None:
            moeda = self.pega_objeto(nome)
            if moeda is not None:
                new_moeda = self.__tela.cadastrar_dados()
                moeda.nome = new_moeda['nome']
                moeda.regioes = new_moeda['regioes']
                moeda.cifra = new_moeda['cifra']
                moeda.valor_usd = new_moeda['valor']
                self.__relatorio.add_operacao('alteracao', f"Alteracao da Moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                MoedaNaoEncontrada
            
    def mostra_todas(self):
        dados_moedas = []
        try:
            for moeda in self.__moeda_DAO.get_all():
                dados_moedas.append({'nome':moeda.nome, 'regioes':moeda.regioes, 'cifra':moeda.cifra, 'valor':moeda.valor_usd})
            self.__tela.mostrar_tabela(dados_moedas)
            self.__relatorio.add_operacao('mostragem', f"Mostragem de todas as moedas registradas, {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
        except FileNotFoundError:
            NenhumRegistrado('moeda')
        
    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()


    def mostra_dados(self):
        nome = self.__tela.ver_dados()
        for moeda in self.__moeda_DAO.get_all():
            if nome.lower() == moeda.nome.lower():
                self.__tela.mostrar_tabela([{'nome': moeda.nome, 'regioes': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd}])
                self.__relatorio.add_operacao('mostragem', f"Mostragem de dados da moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
