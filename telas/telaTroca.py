from abstratas.absTela import Tela
import PySimpleGUI as sg
from funcoes import *
from datetime import datetime as dt


class TelaTroca(Tela):
    def __init__(self):
        self.__window = None
        self.tela_opcoes()
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
            [sg.Radio("1 - Ver dados de uma Troca", "RDT", key='1')],
            [sg.Radio("2 - Adicionar Troca", "RDT", key='2')],
            [sg.Radio("3 - Excluir Troca", "RDT", key='3')],
            [sg.Radio("4 - Listar todas as Trocas", "RDT", key='4')],
            [sg.Radio("5 - Alterar dados de uma Troca", "RDT", key='5')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("TROCAS").Layout(layout)
        
        
    def ver_dados(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Escreva o id da troca que deseja achar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id']    
        
    
    def cadastrar_dados(self):
        sg.change_look_and_feel("LightGreen1")
        layout = [ 
            [sg.Text('--------INFORMAÇÕES DA TROCA--------')],
            [sg.Text(f'ID DA TROCA: '), sg.InputText('', key='id')],
            [sg.Text(f'CPF DA PESSOA: '), sg.InputText('', key='cpf')],
            [sg.Text(f'MOEDA ENTRADA: '), sg.InputText('', key='nome_moeda_entrada')],
            [sg.Text(f'MOEDA SAIDA: '), sg.InputText('', key='nome_moeda_saida')],
            [sg.Text(f'QUANTIDADE ENTRADA: '), sg.InputText('', key='quantidade_entrada')],
            [sg.Text(f'JUROS: '), sg.InputText('', key='juros')],
            [sg.Text(f'DATA: '), sg.InputText('', key='data')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        
        id = valores['id']
        cpf = valores['cpf']
        nome_moeda_entrada = valores['nome_moeda_entrada']
        nome_moeda_saida = valores['nome_moeda_saida']
        data = valores['data']
        corretos = True
        if botao not in (None, 'Cancelar'):
            if id in (None, ''):
                CampoVazio('id')
                corretos = False
                          
            try:
                quantidade_entrada = float(valores['quantidade_entrada'])
            except:
                NaoNumericoGeral("'quantidade entrada'")
                corretos = False
                
            try:
                juros = float(valores['juros'])
                if juros < 0:
                    JurosNegativo()
            except:
                NaoNumericoGeral('juros')
                corretos = False
                
            if corretos:
                return {'id': id, 'id_pessoa': cpf, 'quantidade_entrada': quantidade_entrada, 'quantidade_saida': 0, 
                        'nome_moeda_entrada': nome_moeda_entrada, 'nome_moeda_saida': nome_moeda_saida, 'juros': juros, 'data':data}
    
    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id da troca que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id'] 

    def alterar_dados(self):
        sg.change_look_and_feel('DarkBrown7')
        layout = [
            [sg.Text('Escreva o id da troca que deseja alterar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id'] 
    
    
    def mostrar_tabela(self, dados_troca):
        sg.change_look_and_feel('DarkTeal4')
        trocas = []
        keys = ['ID', 'CPF', 'Data', 'Moeda Entregue', 'Moeda Recebida', 'Quantidade da Moeda Entregue', 'Quantidade da Moeda Recebida', 'Juros']
        for t in dados_troca:
            trocas.append(list(t.values()))
        layout = [
            [sg.Text("TROCAS REGISTRADAS")],
            [sg.Table(values =trocas,
                    headings =keys,
                    auto_size_columns= True,
                    justification='center',
                    expand_x=True,
                    expand_y=True,
                    vertical_scroll_only=False,
                    num_rows= len(dados_troca))],
            [sg.Button("OK")]
        ]
        window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS", layout, size=(700, 350))
        
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "OK"):
                window.close()
                break

    