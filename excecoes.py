import PySimpleGUI as sg


class OpcaoDigitadaIncorretamente():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nOpção digitada incorretamente. Tente Novamente\n" 
        sg.Popup(self.msg)

class NaoNumericoGeral():
    def __init__(self, variavel):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nO valor de {variavel} digitado não é numérico\n"
        sg.Popup(self.msg)

class NomeComDigito():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNão pode haver números ou dígitos no nome\n"
        sg.Popup(self.msg)

class IdNaoNumerico():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNão pode haver caracteres não numéricos na identidade dos Clientes\n"
        sg.Popup(self.msg)

class NaoInteiro():
    def __init__(self, variavel):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nO valor de {variavel} precisa ser um Número e ser Inteiro\n"
        sg.Popup(self.msg)

class NaoFoiEncontradoComEsteId():
    def __init__(self, tipo):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNao foi encontrado(a) {tipo} registrado(a) com este id\n"
        sg.Popup(self.msg)

class MoedaNaoEncontrada():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNao foi encontrada moeda registrada com este nome\n"
        sg.Popup(self.msg)
        
class NenhumRegistrado():
    def __init__(self, tipo):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNão há {tipo}(s) registrados(as)\n"
        sg.Popup(self.msg)          

class TamanhoErradoId():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nId com o tamanho errado: CPF deve ter 3 digitios e CNPJ 5.\n"
        sg.Popup(self.msg)

class NomeVazio():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNome não pode ser um campo vazio\n"
        sg.Popup(self.msg)
