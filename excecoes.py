import PySimpleGUI as sg


class OpcaoDigitadaIncorretamente(Exception):
    def __init__(self):
        self.msg = f"\nOpção digitada incorretamente. Tente Novamente\n" 
        sg.Popup(self.msg)

class NaoNumericoGeral(Exception):
    def __init__(self, variavel):
        self.msg = f"\nO valor de '{variavel}' digitado não é numérico\n"
        sg.Popup(self.msg)

class NomeComDigito(Exception):
    def __init__(self):
        self.msg = f"\nNão pode haver números ou dígitos no nome\n"
        sg.Popup(self.msg)

class IdNaoNumerico(Exception):
    def __init__(self):
        self.msg = f"\nNão pode haver caracteres não numéricos na identidade do Clientes\n"
        sg.Popup(self.msg)

class NaoInteiro(Exception):
    def __init__(self, variavel):
        self.msg = f"\nO valor de '{variavel}' precisa ser um Número e ser Inteiro\n"
        sg.Popup(self.msg)

class NaoFoiEncontradoComEsteId(Exception):
    def __init__(self, tipo):
        self.msg = f"\n## Nao foi encontrado {tipo} registrado com este id ##\n"
        sg.Popup(self.msg)

class MoedaNaoEncontrada(Exception):
    def __init__(self):
        self.msg = f"\n## Nao foi encontrada moeda registrada com este nome ##\n"
        sg.Popup(self.msg)
        
class NenhumRegistrado(Exception):
    def __init__(self, tipo):
        self.msg = f"\n## Não há {tipo}(s) registrados(as) ##\n"
        sg.Popup(self.msg)          
