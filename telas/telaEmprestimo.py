from abstratas.absTela import Tela
from datetime import datetime
import PySimpleGUI as sg


class TelaEmprestimo(Tela):
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
        if botao in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao
    
    def tela_opcoes(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Radio("1 - Ver empréstimo registrado", "RDE", key='1')],
            [sg.Radio("2 - Registrar empréstimo", "RDE", key='2')],
            [sg.Radio("3 - Excluir empréstimo", "RDE", key='3')],
            [sg.Radio("4 - Listar todos empréstimos", "RDE", key='4')],
            [sg.Radio("5 - Alterar empréstimo", "RDE", key='5')],
            [sg.Radio("6 - Registrar devolução de empréstimo", "RDE", key='6')],
            # [sg.Radio("7 - Calcular valor de juros de um empréstimo", "RDE", key='7')],
            [sg.Cancel('Voltar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("EMPRESTIMOS").Layout(layout)        
        
        
    def ver_dados(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id do emprestimo que deseja ver: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar') :
            return valores['id']
    

    def cadastrar_dados(self):
        layout = [ 
            [sg.Text('--------INFORMAÇÕES DA MOEDA--------')],
            [sg.Text(f'ID DO EMPRESTIMO: '), sg.InputText('', key='id')],
            [sg.Text(f'ID DO CLIENTE: '), sg.InputText('', key='id_cliente')],
            [sg.Text(f'ID DO EMPRESTADOR: '), sg.InputText('', key='id_emprestador')],
            [sg.Text(f'MOEDA: '), sg.InputText('', key='moeda')],
            [sg.Text(f'QUANTIDADE PEDIDA: '), sg.InputText('', key='quantia_repassada')],
            [sg.Text(f'DATA REPASSADA: '), sg.InputText('', key='data_repasse')],
            [sg.Text(f'DATA DEVOLVIDA: '), sg.InputText('', key='data_devolvida')],
            [sg.Text(f'DATA PRETENDIDA: '), sg.InputText('', key='data_pretendida')],         
            [sg.Text(f'JUROS: '), sg.InputText('', key='juros')],
            [sg.Text(f'JUROS DE ATRASO: '), sg.InputText('', key='juros_atraso')],
            [sg.Text(f'DEVOLVIDO'), sg.Radio("SIM", "DEVOLVIDO", key="sim"),  sg.Radio("NÃO", "DEVOLVIDO", key="nao", default=True)],     
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            id = valores['id']
            id_cliente = valores['id_cliente']
            id_emprestador = valores['id_emprestador']
            moeda = valores['moeda']
            quantia_repassada = float(valores['quantia_repassada'])
            data_do_repasse = valores['data_repasse']
            data_devolvida = valores['data_devolvida']
            data_pretendida = valores['data_devolvida']
            juros_normal = float(valores['juros'])
            juros_mensal_atraso = float(valores['juros_atraso'])
            if valores['sim']:
                devolvido = True
            else:
                devolvido = False
            self.close()
            return {'id':id, 'cliente_id':id_cliente, 'emprestador_id':id_emprestador, 'moeda':moeda, 'quantia_repassada':quantia_repassada, 
                    'data_do_repasse':data_do_repasse, 'data_devolvida':data_devolvida, 'data_pretendida':data_pretendida, 
                    'juros_normal':juros_normal, 'juros_mensal_atraso':juros_mensal_atraso, 'devolvido': devolvido}
        # print('-------REGISTRANDO EMPRÉSTIMO--------')
        # try:
        #     id = input('Digite um id novo para a transação: ')
        # except:
        #     print()
        #     print('## O ID deve ser um número ##')
        #     print()
        #     return
        # cliente_id = input('Digite o cpf/cnpj do cliente que pediu o empréstimo: ')
        # emprestador_id = input('Digite o cpf/cnpj do cliente que concedeu: ')
        # moeda = input('Digite o nome da moeda utilizada: ')
        # try:
        #     quantia_repassada = float(input('Digite a quantia repassada nesta moeda: '))
        # except:
        #     print()
        #     print('## O valor digitado não é uma quantia ##')
        #     print()
        # data_do_repasse = input('Digite a data em que foi feito o repasse [dd/mm/aaaa]: ')
        # data_do_repasse = datetime.strptime(data_do_repasse, '%d/%m/%Y')
        # data_pretendida = input('Digite a data máxima combinada para devolução [dd/mm/aaaa]: ')
        # data_pretendida = datetime.strptime(data_pretendida, '%d/%m/%Y')
        # try:
        #     juros_normal = float(input('Digite a quantidade de juros normal (em %) que será aplicado: '))
        #     juros_mensal_atraso = float(input('Digite a quantidade de juros (%) que será aplicado mensalmente em caso de atraso: '))
        # except:
        #     print()
        #     print('## Valor digitado não corresponde a juros ##')
        #     print()
        # dev = int(input('O empréstimo já foi devolvido e está sendo apenas registrado? 0- não, 1- sim: '))
        # if dev == 1:
        #     devolvido = True
        #     data_devolvida = input('Digite a data em que o empréstimo foi devolvido [dd/mm/aaaa]: ')
        #     data_devolvida = datetime.strptime(data_devolvida, '%d/%m/%Y')
        # elif dev == 0:
        #     devolvido = False
        #     data_devolvida = None
            
        # else:
        #     print("## opcao errada ##")
        # return {'id':id, 'cliente_id':cliente_id, 'emprestador_id':emprestador_id, 'moeda':moeda, 'quantia_repassada':quantia_repassada, 
        #         'data_do_repasse':data_do_repasse, 'data_devolvida':data_devolvida, 'data_pretendida':data_pretendida, 
        #         'juros_normal':juros_normal, 'juros_mensal_atraso':juros_mensal_atraso, 'devolvido': devolvido}
    
    
    def excluir(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id do emprestimo que deseja excluir: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id'] 


    def alterar_dados(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id do emprestimo que deseja alterar: '), sg.InputText('', key='id')],           
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id'] 


    def mostrar_tabela(self, dados_emprestimo):
        emprestimo = []
        keys = ['id', 'cliente_id', 'emprestador_id', 'moeda', 'quantia_repassada', 
                'data_do_repasse', 'data_devolvida', 'data_pretendida', 
                'juros_normal', 'juros_mensal_atraso', 'devolvido']
        for e in dados_emprestimo:
            emprestimo.append(list(e.values()))
        layout = [
            [sg.Text("EMPRÉSTIMOS REGISTRADOS")],
            [sg.Table(values =emprestimo,
                    headings =keys,
                    auto_size_columns= True,
                    justification='center',
                    expand_x=True,
                    expand_y=True,
                    vertical_scroll_only=False,
                    num_rows= len(dados_emprestimo))],
            [sg.Button("OK")]
        ]
        window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS", layout, size=(700, 350))
        
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "OK"):
                window.close()
                break


    def ver_juros(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id do empréstimo a qual deseja ver o valor do juros: '), sg.InputText('', key='id')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            return valores['id'] 
        
        
    def emprestimo_devolvido(self):
        sg.change_look_and_feel('DarkRed')
        layout = [
            [sg.Text('Escreva o id do empréstimo a qual se deseja registrar devolução: '), sg.InputText('', key='id')], 
            [sg.Text('Escreva a data em que o dinheiro foi devolvido: '), sg.InputText('', key='data')],          
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window("CASA DE CAMBIO E EMPRÉSTIMOS").Layout(layout)
        botao, valores = self.open()
        self.close()
        if botao not in (None, 'Cancelar'):
            id = valores['id']
            data = datetime.strptime(valores['data'], '%d/%m/%Y')
            return {'id':id, 'data':data}   


