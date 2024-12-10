import PySimpleGUI as sg

class TelaRelatorio():

    def mostra_relatorio(self, msg_lst, titulo):
        soma_de_msg = ''
        for msg in msg_lst:
            soma_de_msg = soma_de_msg + msg + '\n'

        sg.Popup(f'-------- {titulo} ----------', soma_de_msg)


    def mostra_msg(self, msg, titulo):
        sg.Popup(msg, title=titulo)