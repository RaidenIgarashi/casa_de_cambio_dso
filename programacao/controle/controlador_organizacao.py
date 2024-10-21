from programacao.limit.tela_organizacao import Tela_Organizacao
from programacao.entity.organizacao import Organizacao
from programacao.controle.controlador import Controlador

class ControladorOrganizacao(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_organizacao = Tela_Organizacao()
        self.__organizacoes = []

    def pegar_por_id(self, id):
        for organizacoes in self.__organizacoes:
            if organizacoes.id == id:
                return organizacoes
        return None

    def inclui(self):
        dados_organizacao = self.__tela_organizacao.pegar_dados()
        self.__organizacoes.append(Organizacao(dados_organizacao['nome'], dados_organizacao['id'], 0))

    def exclui(self):
        id = self.__tela_organizacao.selecionar()
        organizacao = self.pegar_por_id(id)
        if not organizacao == None:
            self.__organizacoes.remove(organizacao)
        else:
            self.__tela_organizacao.mostra_msg('Organização não existe')

    def listar(self):
        for organizacao in self.__organizacoes:
            self.__tela_organizacao.monstrar({'nome': organizacao.nome, 'id': organizacao.id, 'credito_usd': organizacao.credito_usd})

    def altera(self):
        self.listar()
        id = self.__tela_organizacao.selecionar()
        organizacao = self.pegar_por_id(id)
        if organizacao != None:
            for org in self.__organizacoes:
                if org.id == organizacao.id:
                    new_org = self.__tela_organizacao.pegar_dados()
                    org.nome = new_org['nome']
                    org.id = new_org['id']
        else:
            self.__tela_organizacao.mostra_msg('Organização não existe')
                    

    def abre_tela(self):
        command_list = {0: self.retornar, 1: self.inclui, 2: self.exclui, 3: self.listar, 4: self.altera}

        continuar = True
        while continuar:
            command_list[self.__tela_organizacao.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()


