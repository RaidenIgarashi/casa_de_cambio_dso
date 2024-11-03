from telas.telaTroca import TelaTroca
from abstratas.absControlador import Controlador
from entidades.troca import Troca

class ControladorTroca(Controlador):
    def __init__(self, controlador_sistema, controlador_moeda, controlador_cliente):
        self.__trocas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaTroca()
        self.__moeda = controlador_moeda
        self.__pessoa = controlador_cliente

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        dados['quantidade_saida'] = self.calculo_moeda_saida(dados['moeda_entrada'], dados['moeda_saida'], dados['quantidade_entrada'], dados['juros'])
        self.__trocas.append(Troca(dados['id'], self.__pessoa.pega_objeto(dados['id_pessoa']), dados['quantidade_entrada'], dados['quantidade_saida'], dados['data'], self.__moeda.pega_objeto(dados['moeda_entrada']), self.__moeda.pega_objeto(dados['moeda_saida']), dados['juros']))

    def exclui(self):
        id = self.__tela.excluir()
        troca = self.pega_objeto(id)
        if troca is not None:
            self.__trocas.remove(troca)

    def altera(self):
        id = self.__tela.alterar_dados()
        troca = self.pega_objeto(id)
        if troca is not None:
            new_dados = self.__tela.cadastrar_dados()
            troca.id = new_dados['id']
            troca.pessoa = self.__pessoa.pega_objeto(new_dados['id_pessoa'])
            troca.quantidade_entrada = new_dados['quantidade_entrada']
            troca.quantidade_saida = self.calculo_moeda_saida(new_dados['moeda_entrada'], new_dados['moeda_saida'], new_dados['quantidade_entrada'], new_dados['juros'])
            troca.data = new_dados['data']
            troca.moeda_entrada = self.__moeda.pega_objeto(new_dados['moeda_entrada'])
            troca.moeda_saida = self.__moeda.pega_objeto(new_dados['moeda_saida'])
            troca.porcentagem_juros = new_dados['juros']
        else:
            print('## não foi encontrado troca com esse ID ##')


    def mostra_dados(self):
        id = self.__tela.ver_dados()
        troca = self.pega_objeto(id)
        self.__tela.mostrar_dados({'id': troca.id, 'id_pessoa':troca.pessoa.cpf, 'data': troca.data, 'moeda_entrada': troca.moeda_entrada.nome, 'moeda_saida': troca.moeda_saida.nome, 'quantidade_entrada': troca.quantidade_entrada, 'quantidade_saida': troca.quantidade_saida, 'juros': troca.porcentagem_juros })

    def mostra_todas(self):
        for troca in self.__trocas:
            self.__tela.mostrar_dados({'id': troca.id, 'id_pessoa':troca.pessoa.cpf, 'data': troca.data, 'moeda_entrada': troca.moeda_entrada.nome, 'moeda_saida': troca.moeda_saida.nome, 'quantidade_entrada': troca.quantidade_entrada, 'quantidade_saida': troca.quantidade_saida, 'juros': troca.porcentagem_juros })

    def calculo_moeda_saida(self, moeda1_nome, moeda2_nome, quantidade_entrada, juros):
        moeda_entrada = self.__moeda.pega_objeto(moeda1_nome)
        moeda_saida = self.__moeda.pega_objeto(moeda2_nome)
        valor_total = quantidade_entrada * moeda_entrada.valor_usd
        valor_total -= valor_total* juros
        return valor_total/moeda_saida.valor_usd

    def pega_objeto(self, id):
        for troca in self.__trocas:
            if id == troca.id:
                return troca
        return None

    def abre_tela(self):
        commandlst = {0: self.volta_tela, 1: self.inclui, 2: self.exclui, 3: self.mostra_todas, 4: self.altera}
        
        while True:
            commandlst[self.__tela.tela_opcoes()]()

    def volta_tela(self):
        self.__controlador_sistema.abre_tela()



