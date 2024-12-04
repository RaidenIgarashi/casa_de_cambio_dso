class Relatorio():
    def __init__(self):
        self.__insercoes = []
        self.__alteracoes = []
        self.__exclusoes = []
        self.__mostragens = []
        
    def add_operacao(self, tipo, dados):
        if tipo == 'exclusao':
            self.__insercoes.append('')
        elif tipo == 'insercao':
            self.__alteracoes.append('')
        elif tipo == 'alteracao':
            self.__exclusoes.append('')
        elif tipo == 'mostragem':
            self.__mostragens.append('')
