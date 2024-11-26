class OpcaoDigitadaIncorretamente(Exception):
    def __init__(self):
        self.msg = 'Opção digitada incorretamente. Tente Novamente'
        super().__init__(self.msg)

class ValorNaoNumerico(Exception):
    def __init__(self):
        self.msg = 'Esse valor não é numérico'
        super().__init__(self.msg)
