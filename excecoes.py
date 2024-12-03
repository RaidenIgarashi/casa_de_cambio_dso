class OpcaoDigitadaIncorretamente(Exception):
    def __init__(self):
        self.msg = 'Opção digitada incorretamente. Tente Novamente'
        super().__init__(self.msg)

class ValorNaoNumerico(Exception):
    def __init__(self):
        self.msg = 'O valor digitado não é numérico'
        super().__init__(self.msg)

class NomeComDigito(Exception):
    def __init__(self):
        self.msg = f'Não pode haver números ou dígitos no nome'
        super().__init__(self.msg)

class ComCaractere(Exception):
    def __init__(self, tipo_correto):
        self.msg = f'Só pode haver {tipo_correto} na identidade do Cliente'
        super().__init__(self.msg)

class NaoInteiro(Exception):
    def __init__(self, var):
        self.msg = f'O valor de {var} não é um número, ou não é um Inteiro'
        super().__init__(self.msg)
