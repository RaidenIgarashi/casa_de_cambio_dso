import PySimpleGUI as sg

class TelaInicializador():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_opcoes(self):
        self.init_components()
        botao, valores = self.__window.Read()
        opcao = 0
        if valores['1']:
            opcao = 1
        if valores['2']:
            opcao = 2
        if valores['3']:
            opcao = 3
        if valores['4']:
            opcao = 4
        if valores['5']:
            opcao = 5
        if valores['6']:
            opcao = 6
        if botao in (None, 'X'):
            opcao = 0
        self.__window.Close()
        return opcao

    def init_components(self):
        sg.change_look_and_feel("DarkGrey11")
        layout = [
            [sg.Text("OPÇÕES:")],
            [sg.Radio("1 - Clientes", "RDI", key='1')],
            [sg.Radio("2 - Moedas", "RDI", key='2')],
            [sg.Radio("3 - Trocas", "RDI", key='3')],
            [sg.Radio("4 - Empréstimos", "RDI", key='4')],
            [sg.Radio("5 - Gerar Relatório", "RDI", key='5')],
            [sg.Radio("6 - Relatório de ações desta sessão", "RDI", key='6')],
            [sg.Cancel(' X '), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)        
        