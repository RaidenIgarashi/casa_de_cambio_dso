class OpcaoDigitadaIncorretamente(Exception):
    def __init__(self):
        self.msg = 'Opção digitada incorretamente. Tente Novamente'
        super().__init__(self.msg)

class NaoNumericoGeral(Exception):
    def __init__(self, variavel):
        self.msg = f"O valor de '{variavel}' digitado não é numérico"
        super().__init__(self.msg)

class NomeComDigito(Exception):
    def __init__(self):
        self.msg = f'Não pode haver números ou dígitos no nome'
        super().__init__(self.msg)

class IdNaoNumerico(Exception):
    def __init__(self):
        self.msg = f'Não pode haver caracteres não numéricos na identidade do Clientes'
        super().__init__(self.msg)

class NaoInteiro(Exception):
    def __init__(self, variavel):
        self.msg = f"O valor de '{variavel}' precisa ser um Número e ser Inteiro"
        super().__init__(self.msg)

class NenhumClienteRegistrado(Exception):
    def __init__(self):
        self.msg = "\n## Nenhum cliente registrado com esta identidade ##\n"
        super().__init__(self.msg)
        
