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
    def mostrar_msg(self, msg):
        sg.Popup(msg)
        
    
    def init_opcoes(self):
        self.tela_opcoes()
        botao, valores = self.open()
        opcao = 0
        for x in range(1, 7):
            if valores[f'{x}']:
                opcao = x
        if botao in (None, 'Voltar', 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
      
    def tela_opcoes(self):
        sg.change_look_and_feel("DarkGrey11")
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
    

    def ver_dados(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja ver: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar') and eh_numerico(valores['id'], "identidade"):
            return valores['id']
    

    def cadastrar_dados(self):
        sg.change_look_and_feel("LightGreen1")
        layout = [ 
            [sg.Text('--------CADASTRAR INFORMAÇÕES DO CLIENTE--------')],
            [sg.Radio('1 - Cadastrar Pessoa Física', 'cli', key='1')],
            [sg.Radio('2 - Cadastrar Empresa/Organização', 'cli', key='2')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()

        if botao not in (None, 'Cancelar'):
            layout = [
                [sg.Text(f'NOME: '), sg.InputText('', key='nome')],
                [sg.Text(f'IDENTIDADE (cpf/cpnj): '), sg.InputText('', key='id')],
            ]
            pessoa = False
            if valores['1']:
                layout.append([sg.Text(f'IDADE: '), sg.InputText('', key='idade')])
                pessoa = True
            layout.append([sg.Cancel('Cancelar'), sg.Button('Confirmar')])

            self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
            botao, valores = self.open()
            self.close()
        
        if botao not in (None, 'Cancelar'):
            nome, id = valores['nome'], valores['id']
            if pessoa:
                idade = valores['idade']

            corretos = True
            if not eh_numerico(id, 'cpf/cnpj'):
                corretos = False
                IdNaoNumerico()
            elif (pessoa and len(id) != 3) or (not pessoa and len(id) != 5): # cpf deve ter 3 digitos e cnpj 5
                corretos = False
                TamanhoErradoId()
            if nome == '':
                corretos = False
                CampoVazio('nome')
            elif pessoa:
                for char in nome:      # nome de pessoa precisa ser só letras
                    if char.isnumeric():
                        corretos = False
                        NomeComDigito()
                        break
            if pessoa:
                try:   # idade precisa ser inteiro
                    idade = int(idade)
                except:
                    corretos = False
                    NaoInteiro('idade')
            
            if corretos:         # se algo estiver errado retorna None
                lista = {"nome": nome, "id": id}
                if pessoa:
                    lista["idade"] = idade
                return lista             
    
    
    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar') and eh_numerico(valores['id'], "cpf/cnpj"):
            return valores['id']       
        

    def alterar_dados(self):
        sg.change_look_and_feel("DarkBrown7")
        layout = [
            [sg.Text('Escreva o CPF/CNPJ do cliente que deseja alterar: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar') and eh_numerico(valores['id'], "cpf/cnpj"):
            return valores['id']
        
    
    def mostrar_tabela(self, dados_cliente, tipo):
        sg.change_look_and_feel('DarkTeal4')
        client = []
        keys = []
        if tipo == 0:
            keys = ["nome", "cnpj"]
            tipo_cliente = "ORGANIZAÇÕES"
        elif tipo == 1:
            keys = ["nome", "cpf", "idade"]
            tipo_cliente = "PESSOAS"
        for d in dados_cliente:
            client.append(list(d.values()))
        layout = [
            [sg.Text(f"{tipo_cliente} REGISTRADAS")],
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
    
    
    def ver_transacoes(self):
        sg.change_look_and_feel('DarkBlue1')
        layout = [
            [sg.Text('Digite o cpf/cnpj do cliente que deseja ver as transações: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        
        if botao not in (None, 'Cancelar') and eh_numerico(valores['id'], "cpf/cnpj"):
            return valores['id']
        
