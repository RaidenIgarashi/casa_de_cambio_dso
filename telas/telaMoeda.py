from abstratas.absTela import Tela
from excecoes import *
import PySimpleGUI as sg
from funcoes import *


class TelaMoeda(Tela):
    def __init__(self):
        self.__window = None
    def close(self):
        self.__window.Close()
    def open(self):
        botao, valores = self.__window.Read()
        return botao, valores
    def mostrar_msg(self, msg):
        sg.Popup(msg)
        

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
    
    def tela_opcoes(self):
        sg.change_look_and_feel("DarkGrey11")
        layout = [
            [sg.Radio("1 - Ver dados Moeda", "RDM", key='1')],
            [sg.Radio("2 - Adicionar Moeda", "RDM", key='2')],
            [sg.Radio("3 - Excluir Moeda", "RDM", key='3')],
            [sg.Radio("4 - Listar todas as Moedas", "RDM", key='4')],
            [sg.Radio("5 - Alterar Moeda", "RDM", key='5')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("MOEDAS").Layout(layout)
    
    
    def ver_dados(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja achar: '), sg.InputText('', key='nome')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['nome']
    

    def cadastrar_dados(self):
        sg.change_look_and_feel("LightGreen1")
        layout = [ 
            [sg.Text('--------INFORMAÇÕES DA MOEDA--------')],
            [sg.Text(f'NOME: '), sg.InputText('', key='nome')],
            [sg.Text(f'REGIOES: '), sg.InputText('', key='regioes')],
            [sg.Text(f'CIFRA: '), sg.InputText('', key='cifra')],
            [sg.Text(f'VALOR EM U$D: '), sg.InputText('', key='valor')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        nome = valores['nome']
        regioes = valores['regioes']
        cifra = valores['cifra']
        valor = valores['valor']
        self.close()

        if botao not in (None, 'Cancelar'):
            corretos = True
            if not eh_alpha(nome):
                corretos = False
            for regiao in regioes:
                if not eh_alpha(regiao):
                    corretos = False
            for c in cifra:
                if c.isnumeric():
                    corretos = False
                    CifraComNumero()
            try:
                if '.' not in valor:
                    valor = int(valor)
                valor = float(valor)
            except:
                corretos = False
                NaoNumericoGeral('Valor')
            
            if corretos:
                return {"nome": nome, "regioes": regioes, "cifra": cifra, "valor": valor}
        

    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja excluir: '), sg.InputText('', key='nome')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['nome']
    

    def alterar_dados(self):
        sg.change_look_and_feel("DarkBrown7")
        layout = [
            [sg.Text('Escreva o nome da moeda que deseja alterar: '), sg.InputText('', key='nome')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['nome']
    
    
    def mostrar_tabela(self, dados_moeda):
        sg.change_look_and_feel('DarkTeal4')
        moeda = []
        keys = ['nome', 'regiao', 'cifra', 'valor_usd']
        for m in dados_moeda:
            moeda.append(list(m.values()))
        layout = [
            [sg.Text("MOEDAS REGISTRADAS")],
            [sg.Table(values =moeda,
                    headings =keys,
                    auto_size_columns= True,
                    justification='center',
                    expand_x=True,
                    expand_y=True,
                    num_rows= len(dados_moeda))],
            [sg.Button("OK")]
        ]
        window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS", layout, size=(350, 450))
        
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "OK"):
                window.close()
                break
    
