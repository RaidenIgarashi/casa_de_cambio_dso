from abstratas.absTela import Tela
from telas.telaRelatorio import TelaRelatorio

class Relatorio():
    def __init__(self):
        self.__inclusoes = []
        self.__alteracoes = []
        self.__exclusoes = []
        self.__mostragens = []
        self.__indefinidos = []
        self.__tela = TelaRelatorio()
        
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
            if lista_operacao[opr] == []:
                if nome[opr] != 'indefinição':
                    self.__tela.mostra_msg(f'\nNenhuma {nome[opr]} foi registrada.\n', titulo[opr])
            else:
                self.__tela.mostra_relatorio(lista_operacao[opr], titulo[opr])
         

