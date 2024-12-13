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
        if dados != None:
            ja_add = self.pega_objeto(dados['nome'])
            if ja_add == None and dados != None:
                self.__moeda_DAO.add(Moeda(dados['nome'], dados['regioes'], dados['cifra'], dados['valor']))
                self.__tela.mostrar_msg(f'Moeda {dados['nome']} adicionada com sucesso')
                self.__relatorio.add_operacao('inclusao', f"Inclusao da Moeda '{dados['nome']}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            elif ja_add != None:
                MoedaJaRegistrada()
            

    def exclui(self):
        nome = self.__tela.excluir()
        if nome != None:
            moeda = self.pega_objeto(nome)
            if moeda != None:
                self.__moeda_DAO.remove(moeda.nome)
                self.__tela.mostrar_msg(f'A moeda {moeda.nome} foi excluida com sucesso')
                self.__relatorio.add_operacao('exclusao', f"Exclusao da Moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                MoedaNaoEncontrada()

    def pega_objeto(self, nome):
        if nome != None:
            for moeda in self.__moeda_DAO.get_all():
                if nome.lower() == moeda.nome.lower():
                    return moeda     
                

    def altera(self):
        nome = self.__tela.alterar_dados()
        if nome != None:
            for m in self.__moeda_DAO.get_all():
                if m.nome == nome:
                    moeda = self.pega_objeto(nome)
                    new_moeda = self.__tela.cadastrar_dados()
                    moeda.nome = new_moeda['nome']
                    moeda.regioes = new_moeda['regioes']
                    moeda.cifra = new_moeda['cifra']
                    moeda.valor_usd = new_moeda['valor']
                    self.__moeda_DAO.update(moeda)
                    self.__relatorio.add_operacao('alteracao', f"Alteracao da Moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
                    self.__tela.mostrar_msg(f'Moeda "{moeda.nome}" alterada com sucesso.')
                    return
            MoedaNaoEncontrada(nome)
        else:
            MoedaNaoEncontrada()
            
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
        if nome != None:
            existe = False
            for moeda in self.__moeda_DAO.get_all():
                if nome.lower() == moeda.nome.lower():
                    self.__tela.mostrar_tabela([{'nome': moeda.nome, 'regioes': moeda.regioes, 'cifra': moeda.cifra, 'valor': moeda.valor_usd}])
                    self.__relatorio.add_operacao('mostragem', f"Mostragem de dados da moeda '{moeda.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
                    existe = True
                    break
            if not existe:
                MoedaNaoEncontrada()
