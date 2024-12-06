from abstratas.absTela import Tela
from excecoes import *
import PySimpleGUI as sg

class TelaMoeda(Tela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    def close(self):
        self.__window.Close()
    def open(self):
        botao, valores = self.__window.Read()
        return botao, valores

    def tela_opcoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Radio("1 - Ver dados Moeda", "RDM", key='1')],
            [sg.Radio("2 - Inclui Moeda", "RDM", key='2')],
            [sg.Radio("3 - Excluir Moeda", "RDM", key='3')],
            [sg.Radio("4 - Listar todas as Moedas", "RDM", key='4')],
            [sg.Radio("5 - Alterar Moeda", "RDM", key='5')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("MOEDAS").Layout(layout)

    def init_opcoes(self):
        self.tela_opcoes()
        botao, valores = self.open()
        opcao = 0
        for x in range(1, 6):
            if valores[f'{x}']:
                opcao = x
        if botao in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def cadastrar_dados(self):
        layout = [ 
            [sg.Text('--------INFORMAÇÕES DA MOEDA--------')],
            [sg.Text(f'NOME: '), sg.InputText('', key='nome')],
            [sg.Text(f'REGIOES: '), sg.InputText('', key='regioes')],
            [sg.Text(f'CIFRA: '), sg.InputText('', key='cifra')],
            [sg.Text(f'VALOR EM U$D: '), sg.InputText('', key='valor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        nome = valores['nome']
        regioes = valores['regioes']
        cifra = valores['cifra']
        valor = valores['valor']
        self.close()

        corretos = True
        for char in nome:
            if char.isnumeric():
                corretos = False
                raise NomeComDigito()
        try:
            if '.' not in valor:
                valor = int(valor)
            valor = float(valor)
        except:
            corretos = False
            raise NaoNumericoGeral('Valor')
        
        if corretos:
            return {"nome": nome, "regioes": regioes, "cifra": cifra, "valor": valor}

    def mostrar_dados(self, dados_moeda):
        sg.Popup(
        '--------INFORMAÇÕES DA MOEDA--------',
        f'NOME: {dados_moeda["nome"]}',
        f'REGIOES: {dados_moeda["regioes"]}',
        f'CIFRA: {dados_moeda["cifra"]}',
        f'VALOR: {dados_moeda["valor"]}',
        '\n')

    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja excluir: '), sg.InputText('', key='nome')],           
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        return valores['nome']

    def alterar_dados(self):
        sg.change_look_and_feel('DarkYellow')
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja alterar: '), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        return valores['nome']

    def ver_dados(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja achar: '), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        return valores['nome']

    def mostrar_msg(self, msg):
        sg.Popup(msg)
