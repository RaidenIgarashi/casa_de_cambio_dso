import PySimpleGUI as sg


class OpcaoDigitadaIncorretamente():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nOpção digitada incorretamente. Tente Novamente\n" 
        sg.Popup(self.msg)

class NaoNumericoGeral():
    def __init__(self, variavel):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nO valor de {variavel} digitado não é numérico ou está no formato incorreto\n"
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
    def __init__(self, nome):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNao foi encontrada moeda registrada com o nome '{nome}'\n"
        sg.Popup(self.msg)
        
class NenhumRegistrado():
    def __init__(self, tipo):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNão há {tipo}(s) registrados(as)\n"
        sg.Popup(self.msg)          

class TamanhoErradoId():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nId com o tamanho errado: CPF deve ter 3 digitios e CNPJ 5\n"
        sg.Popup(self.msg)

class CampoVazio():
    def __init__(self, tipo):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nO campo de {tipo} não pode ser  vazio\n"
        sg.Popup(self.msg)

class ClienteJaRegistrado():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nJá existe Cliente registrado com essa identidade\n"
        sg.Popup(self.msg)

class MoedaJaRegistrada():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nJá existe Moeda registrada com este nome\n"
        sg.Popup(self.msg)

class EmprestimoJaRegistrado():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nJá existe Empréstimo registrado com esse id\n"
        sg.Popup(self.msg)

class TrocaJaRegistrada():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nJá existe Troca registrada com esse id\n"
        sg.Popup(self.msg)

class CifraComNumero():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nNão pode haver números na cifra da moeda\n"
        sg.Popup(self.msg)
        
class JurosNegativo():
    def __init__(self):
        sg.change_look_and_feel('DarkRed')
        self.msg = f"\nO juros precisa ser maior ou igual a zero\n"
        sg.Popup(self.msg)
