import PySimpleGUI as sg

class TelaRelatorio():

    def gera_relatorio(self, lista_operacao):
        titulo = ('INCLUSOES: ','ALTERACOES: ','EXCLUSOES: ','MOSTRAGENS: ','INDEFINIDOS: ',)
        nome = ('inclusão','alteração','exclusão','mostragem','indefinição',)
        for opr in range(len(lista_operacao)):
            if lista_operacao[opr] == []:
                if nome[opr] != 'indefinição':
                    self.mostra_msg(f'\nNenhuma {nome[opr]} foi registrada.\n', titulo[opr])
            else:
                self.mostra_relatorio(lista_operacao[opr], titulo[opr])


    def mostra_relatorio(self, msg_lst, titulo):
        soma_de_msg = ''
        for msg in msg_lst:
            soma_de_msg = soma_de_msg + msg + '\n\n'

        self.mostra_msg(f'-------- {titulo} ----------', soma_de_msg)
        

    def mostra_msg(self, msg, titulo):
        sg.Popup(msg, title=titulo)
