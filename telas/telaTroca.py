from abstratas.absTela import Tela
import PySimpleGUI as sg
from funcoes import *


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
        sg.change_look_and_feel('DarkPurple')
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
        layout = [ 
            [sg.Text('--------INFORMAÇÕES DA TROCA--------')],
            [sg.Text(f'ID DA TROCA: '), sg.InputText('', key='id')],
            [sg.Text(f'CPF DA PESSOA: '), sg.InputText('', key='cpf')],
            [sg.Text(f'MOEDA ENTRADA: '), sg.InputText('', key='moeda_entrada')],
            [sg.Text(f'MOEDA SAIDA: '), sg.InputText('', key='moeda_saida')],
            [sg.Text(f'QUANTIDADE ENTRADA: '), sg.InputText('', key='quantidade_entrada')],
            [sg.Text(f'JUROS: '), sg.InputText('', key='juros')],
            [sg.Text(f'DATA: '), sg.InputText('', key='data')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            id = valores['id']
            cpf = valores['cpf']
            moeda_entrada = valores['moeda_entrada']
            moeda_saida = valores['moeda_saida']
            quantidade_entrada = float(valores['quantidade_entrada'])
            juros = float(valores['juros'])
            data = valores['data']
            self.close()
            return {'id': id, 'id_pessoa': cpf, 'quantidade_entrada': quantidade_entrada, 'quantidade_saida': 0, 'moeda_entrada': moeda_entrada, 'moeda_saida': moeda_saida, 'juros': juros, 'data':data}
        # try:
        #     id = int(input('Digite o id da troca: '))
        # except(ValueError):
        #     print()
        #     print('## O ID precisa ser um número sem vígula ##')
        #     print()
        #     return
        # try:
        #     id_pessoa = input('Digite o cpf da pessoa: ')
        #     id_pessoa_verify = id_pessoa.replace('.', '')
        #     if len(id_pessoa_verify) != 3:
        #         raise ValueError('## entrada não corresponde a um cpf ##')
        # except ValueError as e:
        #     print()
        #     print(e)
        #     print()
        #     return
        # moeda_entrada = input('Digite o nome da moeda que o cliente tem para trocar: ')
        # moeda_saida = input('Digite o nome da moeda que o cliente quer receber: ')
        # try:
        #     quantidade_entrada = float(input(f'Digite o quanto de "{moeda_entrada}" o cliente quer trocar por "{moeda_saida}": '))
        # except:
        #     print()
        #     print(' ## Isso não e uma quantia ## ')
        #     print()
        #     return
        # try:
        #     juros = float(input('Digite o juros que será aplicado (em %): ')) / 100
        #     if juros > 1:
        #         raise ValueError
        # except:
        #     print()
        #     print('## O valor escrito não é um juros ##')
        #     print()
        #     return
        # try:
        #     data = input('Digite a data da transação (dd/mm/aaaa): ')
        #     data_sem_barra = data.replace('/', '')
        #     if len(data_sem_barra) != 8:
        #         raise ValueError
        #     data_sem_barra = int(data_sem_barra)
        # except:
        #     print()
        #     print('## esse valor não é uma data ##')
        #     print()
        #     return

        #return {'id': id, 'id_pessoa': id_pessoa, 'quantidade_entrada': quantidade_entrada, 'quantidade_saida': 0, 'moeda_entrada': moeda_entrada, 'moeda_saida': moeda_saida, 'juros': juros, 'data':data}
    
    
    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id da troca que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar') and eh_numerico(valores['id']):
            return valores['id'] 


    def alterar_dados(self):
        sg.change_look_and_feel('LightBrown')
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

    