import PySimpleGUI as sg

class TelaInicializador():
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
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
        if botao in (None, 'ENCERRAR'):
            opcao = 0
        self.__window.Close()
        return opcao

    def init_components(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text("OPÇÕES:")],
            [sg.Radio("1 - Clientes", "RD_init", key='1')],
            [sg.Radio("2 - Moedas", "RD_init", key='2')],
            [sg.Radio("3 - Trocas", "RD_init", key='3')],
            [sg.Radio("4 - Empréstimos", "RD_init", key='4')],
            [sg.Radio("5 - Gerar Relatório", "RD_init", key='5')],
            [sg.Cancel('ENCERRAR'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)        
        