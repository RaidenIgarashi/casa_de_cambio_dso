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
        
    def init_opcoes(self):
        self.tela_opcoes()
        botao, valores = self.open()
        opcao = 0
        for x in range(1, 8):
            if valores[f'{x}']:
                opcao = x
        if botao in (None, 'Voltar'):
            opcao = 0
        self.close()
        return opcao

    def cadastrar_dados(self):
        print('-------REGISTRANDO EMPRÉSTIMO--------')
        try:
            id = input('Digite um id novo para a transação: ')
        except:
            print()
            print('## O ID deve ser um número ##')
            print()
            return
        cliente_id = input('Digite o cpf/cnpj do cliente que pediu o empréstimo: ')
        emprestador_id = input('Digite o cpf/cnpj do cliente que concedeu: ')
        moeda = input('Digite o nome da moeda utilizada: ')
        try:
            quantia_repassada = float(input('Digite a quantia repassada nesta moeda: '))
        except:
            print()
            print('## O valor digitado não é uma quantia ##')
            print()
        data_do_repasse = input('Digite a data em que foi feito o repasse [dd/mm/aaaa]: ')
        data_do_repasse = datetime.strptime(data_do_repasse, '%d/%m/%Y')
        data_pretendida = input('Digite a data máxima combinada para devolução [dd/mm/aaaa]: ')
        data_pretendida = datetime.strptime(data_pretendida, '%d/%m/%Y')
        try:
            juros_normal = float(input('Digite a quantidade de juros normal (em %) que será aplicado: '))
            juros_mensal_atraso = float(input('Digite a quantidade de juros (%) que será aplicado mensalmente em caso de atraso: '))
        except:
            print()
            print('## Valor digitado não corresponde a juros ##')
            print()
        dev = int(input('O empréstimo já foi devolvido e está sendo apenas registrado? 0- não, 1- sim: '))
        if dev == 1:
            devolvido = True
            data_devolvida = input('Digite a data em que o empréstimo foi devolvido [dd/mm/aaaa]: ')
            data_devolvida = datetime.strptime(data_devolvida, '%d/%m/%Y')
        elif dev == 0:
            devolvido = False
            data_devolvida = None
            
        else:
            print("## opcao errada ##")
        return {'id':id, 'cliente_id':cliente_id, 'emprestador_id':emprestador_id, 'moeda':moeda, 'quantia_repassada':quantia_repassada, 
                'data_do_repasse':data_do_repasse, 'data_devolvida':data_devolvida, 'data_pretendida':data_pretendida, 
                'juros_normal':juros_normal, 'juros_mensal_atraso':juros_mensal_atraso, 'devolvido': devolvido}

    def mostrar_dados(self, dados_emprestimo):
        print('--------INFORMAÇÕES DO EMPRÉSTIMO--------')
        print(f'ID: {dados_emprestimo["id"]}')
        print(f'CLIENTE: {dados_emprestimo["cliente_id"]}')
        print(f'EMPRESTADOR: {dados_emprestimo["emprestador_id"]}')
        print(f'VALOR: {dados_emprestimo["quantia_repassada"]} em "{dados_emprestimo["moeda"].nome}"')
        print(f'DATAS: Repassado dia {dados_emprestimo["data_do_repasse"]}, com prazo até {dados_emprestimo["data_pretendida"]}.')
        print(f'JUROS: {dados_emprestimo["juros_normal"]}% + {dados_emprestimo["juros_mensal_atraso"]}% por mês em caso de atraso.')
        if dados_emprestimo['devolvido'] == True:
            print(f'SITUAÇÃO: DEVOLVIDO no dia {dados_emprestimo["data_devolvida"]}')
        else:
            print('SITUAÇÃO: NÃO devolvido')
        print('\n')

    def ver_juros(self):
        id = input('Escreva o id do empréstimo a qual deseja ver o valor do juros: ')
        return id
    def escolher_data(self):
        data = input('Escreva a data em qual se quer ver o possível valor acumulado: ')
        data = datetime.strptime(data, '%d/%m/%Y')
        return data
        
    def emprestimo_devolvido(self):
        id = input('Escreva o id do empréstimo a qual se deseja registrar devolução: ')
        data = input('Escreva a data em que o dinheiro foi devolvido: ')
        data = datetime.strptime(data, '%d/%m/%Y')
        return {'id':id, 'data':data}


    def excluir(self):
        id = input('Escreva o id do empréstimo que deseja excluir: ')
        return id 

    def alterar_dados(self):
        id = input('Escreva o id do empréstimo que deseja alterar: ')
        return id

    def ver_dados(self):
        id = input('Escreva o id do empréstimo que deseja ver: ')
        return id

    def mostrar_msg(self, msg):
        print(msg)
