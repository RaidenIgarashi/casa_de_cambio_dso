from ..limit.tela_organizacao import Tela_Organizacao
from ..entity.organizacao import Organizacao
from controlador import Controlador

class ControladorOrganizacao(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizacao = Tela_Organizacao()
        self.__organizacaos = []

    def inclui(self):
        dados_organizacao = self.__tela_organizacao.pegar_dados()
        self.__organizacaos.append(Organizacao(dados_organizacao['nome'], dados_organizacao['cnpj'], 0))
    
    def exclui(self):
        cnpj = self.__tela_organizacao.selecionar()
        for organizacao in self.__organizacaos:
            if cnpj == organizacao.cnpj:
                self.__organizacaos.remove(organizacao)

    def abre_tela(self):
        command_list = {1: self.inclui, 2: self.exclui, 3: self.altera, 4: self.listar}

        continuar = True
        while continuar:
            command_list[self.__tela_organizacao.tela_opcoes()]()