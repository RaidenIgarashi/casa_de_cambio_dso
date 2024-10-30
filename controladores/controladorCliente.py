from abstratas.absControlador import Controlador
from telas.telaCliente import TelaCliente
from entidades.organizacao import Organizacao
from entidades.pessoa import Pessoa

class ControladorCliente(Controlador):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        self.__pessoas = [Pessoa]
        self.__organizacoes = [Organizacao]

    def eh_pessoa(info): #funcao para facilitar de ver se é pessoa ou organizacao (por id ou por objeto msm)
        if isinstance(info, str):
            for char in info:
                if not char.isnumeric:
                    info = info.replace(char, '')
            if len(info) == 11:
                return True
            elif len(info) == 14:
                return False
            else:
                pass #aqui depois tem que chamar o erro de cpf invalido
        elif isinstance(info, Pessoa):
            return True
        elif isinstance(info, Organizacao):
            return False
        else:
            pass #aqui depois tem que chamar o erro de tipo colocado invalido  

    def abre_tela(self):
        command_list = {1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.altera, 5: self.mostra_todas, 0: self.voltar_tela}
        continuar = True
        while continuar:
            command_list[self.__tela_cliente.tela_opcoes()]()

    def mostra_dados(self, id):
        if eh_pessoa(id): #cpf
            for pessoa in self.__pessoas:
                if pessoa.id == id:
                    self.__tela_cliente.mostrar({'nome': pessoa.nome, 'id': pessoa.id, 'credito_usd': pessoa.credito_usd})
        else: #cnpj
            for org in self.__organizacoes:
                if org.id == id:
                    self.__tela_cliente.mostrar({'nome': org.nome, 'id': org.id, 'credito_usd': org.credito_usd})

    def pega_objeto(self, id):
        if eh_pessoa(id): #cpf
            for pessoa in self.__pessoas:
                if pessoa.id == id:
                    return pessoa
        else: #cnpj
            for org in self.__organizacoes:
                if org.id == id:
                    return org

    def inclui(self):
        dados_cliente = self.__tela_cliente.cadastrar_dados()
        if len(dados_cliente) == 2:#colocar eh dados
            self.__organizacoes.append(Organizacao(dados_cliente['nome'], dados_cliente['id'], 0))
        elif len(dados_cliente) == 3:
            self.__organizacoes.append(Pessoa(dados_cliente['nome'], dados_cliente['id'], 0, dados_cliente['idade']))

    def exclui(self):
        id = self.__tela_cliente.selecionar()
        cliente = self.pega_objeto(id)
        if not cliente == None:
            self.__organizacoes.remove(cliente)
        else:
            self.__tela_cliente.mostrar_msg('Organização não existe')

    def mostra_todas(self):
        for org in self.__organizacoes:
            self.__tela_cliente.mostrar({'nome': org.nome, 'id': org.id, 'credito_usd': org.credito_usd})
        for pessoa in self.__pessoas:
            self.__tela_cliente.mostrar({'nome': pessoa.nome, 'id': pessoa.id, 'idade': pessoa.idade, 'credito_usd': pessoa.credito_usd})

    def altera(self):
        self.mostra_todas()
        id = self.__tela_cliente.selecionar()
        id_a_alterar = self.pega_objeto(id)
        if id_a_alterar != None:
            lista = self.__pessoas if len(id) == 11 else self.__organizacoes
            for cliente in lista:
                if cliente.id == id_a_alterar.id:
                    novo_cliente = self.__tela_cliente.cadastrar_dados()
                    cliente.nome = novo_cliente['nome']
                    cliente.id = novo_cliente['id']
                    if len(id) == 11:
                        cliente.idade = novo_cliente['idade']
        else:
            self.__tela_cliente.mostrar_msg('Organização não existe')

    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()

