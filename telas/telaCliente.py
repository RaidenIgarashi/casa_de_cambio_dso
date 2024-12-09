from abstratas.absTela import Tela
from funcoes import *
from excecoes import *
from funcoes import *
import PySimpleGUI as sg


class TelaCliente(Tela):
    def __init__(self):
        self.__window = None
        self.tela_opcoes()
    def close(self):
        self.__window.Close()
    def open(self):
        botao, valores = self.__window.Read()
        return botao, valores
        
    def tela_opcoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Radio("1 - Ver dados de um Cliente", "RDC", key='1')],
            [sg.Radio("2 - Adicionar Cliente", "RDC", key='2')],
            [sg.Radio("3 - Excluir Cliente", "RDC", key='3')],
            [sg.Radio("4 - Listar todos Clientes", "RDC", key='4')],
            [sg.Radio("5 - Alterar Cliente", "RDC", key='5')],
            [sg.Radio("6 - Ver Transações de um Cliente", "RDC", key='6')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CLIENTES").Layout(layout)

    
    def init_opcoes(self):
        self.tela_opcoes()
        botao, valores = self.open()
        opcao = 0
        for x in range(1, 7):
            if valores[f'{x}']:
                opcao = x
        if botao in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def ver_dados(self):
        sg.change_look_and_feel('Purple')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja achar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id'], "identidade"):
            return valores['id']
    

    def cadastrar_dados(self):
        layout = [ 
            [sg.Text('--------CADASTRAR INFORMAÇÕES DO CLIENTE--------')],
            [sg.Radio('1 - Cadastrar Pessoa Física', 'cli', key='1')],
            [sg.Radio('2 - Cadastrar Empresa/Organização', 'cli', key='2')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()

        layout = [
            [sg.Text(f'NOME: '), sg.InputText('', key='nome')],
            [sg.Text(f'IDENTIDADE (cpf/cpnj): '), sg.InputText('', key='id')],
        ]
        pessoa = False
        if valores['1']:
            layout.append([sg.Text(f'IDADE: '), sg.InputText('', key='idade')])
            pessoa = True
        layout.append([sg.Cancel('Voltar'), sg.Button('Confirmar')])

        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        
        nome, id = valores['nome'], valores['id']
        if pessoa:
            idade = valores['idade']

        corretos = True
        for char in nome:      # nome precisa ser só letras
            if char.isnumeric() and pessoa:
                corretos = False
                raise NomeComDigito()
        for char in id:       # id precisa ser só numeros
            if not char.isnumeric():
                corretos = False
                raise IdNaoNumerico
        if pessoa:
            try:   # idade precisa ser inteiro
                int(idade) 
            except:
                corretos = False
                raise NaoInteiro('idade')
        
        if corretos:
            lista = {"nome": nome, "id": id}
            if pessoa:
                lista["idade"] = idade
            return lista 
        else:
            return None        # se algo estiver errado retorna None

    def alterar_dados(self):
        sg.change_look_and_feel('DarkYellow')
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja alterar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id'], "identidade"):
            return valores['id']
    
    def mostrar_dados(self, dados_cliente, tipo):
        client = []
        keys = []
        if tipo == 0:
            keys = ["nome", "cnpj"]
            titulo_tipo_cliente = "ORGANIZAÇÕES"
        elif tipo == 1:
            keys = ["nome", "cpf", "idade"]
            titulo_tipo_cliente = "PESSOAS"
        for d in dados_cliente:
            client.append(list(d.values()))
        layout = [
            [sg.Text("INFORMAÇÕES DOS CLIENTES:" + titulo_tipo_cliente)],
            [sg.Table(values =client,
                    headings =keys,
                    auto_size_columns= True,
                    justification='center',
                    expand_x=True,
                    expand_y=True,
                    num_rows= len(dados_cliente))],
            [sg.Button("OK")]
        ]
        window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS", layout, size=(350, 450))
        
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "OK"):
                window.close()
                break
    
    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id'], "identidade"):
            return valores['id']
    
    def ver_transacoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja ver as transações: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if eh_numerico(valores['id'], "identidade"):
            return valores['id']

    def mostrar_msg(self, msg):
        sg.Popup(msg)
