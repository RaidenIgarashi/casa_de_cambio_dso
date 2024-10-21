from programacao.controlador.controlador import Controlador
from programacao.telas.tela_pessoa import TelaPessoa
from programacao.entidades.pessoa import Pessoa

class ControladorPessoa(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()
        self.__pessoa = []

    def pegar_por_id(self, id):
        for pessoa in self.__pessoa:
            if pessoa.id == id:
                return pessoa
        return None

    def inclui(self):
        dados_pessoa = self.__tela_pessoa.pegar_dados()
        self.__pessoa.append(Pessoa(dados_pessoa['nome'], dados_pessoa['id'], dados_pessoa['idade'], 0))

    def exclui(self):
        id = self.__tela_pessoa.selecionar()
        pessoa = self.pegar_por_id(id)
        if pessoa != None:
            self.__pessoa.remove(pessoa)
        else:
            self.__tela_pessoa.mostra_msg('Pessoa não existe')

    def listar(self):
        for pessoa in self.__pessoa:
            self.__tela_pessoa.mostrar({'nome':pessoa.nome, 'idade':pessoa.idade, 'id':pessoa.id, 'credito_usd':pessoa.credito_usd})

    def altera(self):
        self.listar()
        id = self.__tela_pessoa.selecionar()
        pessoa = self.pegar_por_id(id)
        if pessoa != None:
            for p in self.__pessoa:
                if p.id == pessoa.id:
                    nova_pessoa = self.__tela_pessoa.pegar_dados()
                    p.nome = nova_pessoa['nome']
                    p.idade = nova_pessoa['idade']
                    p.id = nova_pessoa['id']
        else:
            self.__tela_pessoa.mostra_msg('Pessoa não existe')

    def abre_tela(self):
        command_list = {0: self.retornar, 1: self.inclui, 2: self.exclui, 3: self.listar, 4: self.altera}

        continua = True
        while continua:
            command_list[self.__tela_pessoa.tela_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
