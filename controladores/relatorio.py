class Relatorio():
    def __init__(self):
        self.__inclusoes = []
        self.__alteracoes = []
        self.__exclusoes = []
        self.__mostragens = []
        self.__indefinidos = []
        
    def add_operacao(self, tipo: str, info: str):
        if tipo == 'inclusao':
            self.__inclusoes.append(info)
        elif tipo == 'alteracao':
            self.__alteracoes.append(info)
        elif tipo == 'exclusao':
            self.__exclusoes.append(info)
        elif tipo == 'mostragem':
            self.__mostragens.append(info)
        else:
            self.__indefinidos.append(info)
            
    def gera_relatorio(self):
        lista_operacao = (self.__inclusoes, self.__alteracoes, self.__exclusoes,
                  self.__mostragens, self.__indefinidos)
        titulo = ('INCLUSOES: ','ALTERACOES: ','EXCLUSOES: ','MOSTRAGENS: ','INDEFINIDOS: ',)
        nome = ('inclusão','alteração','exclusão','mostragem','indefinição',)
        for opr in range(len(lista_operacao)):
            print('\n', titulo[opr])
            if lista_operacao[opr] == []:
                print(f'\nNenhuma {nome[opr]} foi registrada.\n')
            else:
                for reg in lista_operacao[opr]:
                    print('\n', reg, '\n')

