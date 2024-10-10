from ..limit.tela_organizacao import Tela_Organizacao
from ..entity.organizacao import Organizacao
from controlador import Controlador

class ControladorOrganizacao(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizacao = Tela_Organizacao()
        self.__organizacoes = []

    def pegar_por_cnpj(self, cnpj):
        for organizacoes in self.__organizacoes:
            if organizacoes.cnpj == cnpj:
                return organizacoes
        return None

    def inclui(self):
        dados_organizacao = self.__tela_organizacao.pegar_dados()
        self.__organizacoes.append(Organizacao(dados_organizacao['nome'], dados_organizacao['cnpj'], 0))

    def exclui(self):
        cnpj = self.__tela_organizacao.selecionar()
        organizacao = self.pegar_por_cnpj(cnpj)
        if not organizacao == None:
            self.__organizacoes.remove(organizacao)
        else:
            self.__tela_organizacao.mostra_msg('Organização não existe')

    def listar(self):
        for organizacao in self.__organizacoes:
            self.__tela_organizacao.monstrar({'nome': organizacao.nome, 'cnpj': organizacao.cnpj, 'credito_usd': organizacao.credito_usd})

    def altera(self):
        self.listar()
        cnpj = self.__tela_organizacao.selecionar()
        organizacao = self.pegar_por_cnpj(cnpj)
        if organizacao != None:
            for org in self.__organizacoes():
                if org.cnpj == organizacao.cnpj:
                    new_org = self.__tela_organizacao.pegar_dados()
                    org.nome = new_org['nome']
                    org.cpnj = new_org['cnpj']
        else:
            self.__tela_organizacao.mostra_msg('Organização não existe')
                    

    def abre_tela(self):
        command_list = {1: self.inclui, 2: self.exclui, 3: self.altera, 4: self.listar}

        continuar = True
        while continuar:
            command_list[self.__tela_organizacao.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()


