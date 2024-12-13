from telas.telaTroca import TelaTroca
from abstratas.absControlador import Controlador
from entidades.troca import Troca
from datetime import datetime as dt
from excecoes import *
from DAOs.troca_dao import TrocaDAO

class ControladorTroca(Controlador):
    def __init__(self, controlador_sistema, controlador_moeda, controlador_cliente, relatorio):
        self.__trocas = TrocaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__relatorio = relatorio
        self.__tela = TelaTroca()
        self.__moeda = controlador_moeda
        self.__cliente = controlador_cliente
        
        
    def abre_tela(self):
        opcoes = {0: self.volta_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.mostra_todas, 5: self.altera}
        
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  
                
                
    def mostra_dados(self):
        id = self.__tela.ver_dados()
        if id != None:
            troca = self.pega_objeto(id)
            if troca is None:
                NaoFoiEncontradoComEsteId('troca')
            else:
                self.__tela.mostrar_tabela([{'id': troca.id, 'id_pessoa':troca.pessoa.id, 'data': troca.data, 
                                        'nome_moeda_entrada': troca.moeda_entrada.nome, 'nome_moeda_saida': troca.moeda_saida.nome, 
                                        'quantidade_entrada': troca.quantidade_entrada, 'quantidade_saida': troca.quantidade_saida, 
                                        'juros': troca.porcentagem_juros }])
                self.__relatorio.add_operacao('mostragem', f"Mostragem de dados da troca de id '{troca.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")  
                      

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        if dados != None:
            pessoa_verify = self.__cliente.pega_objeto(dados['id_pessoa'])
            moeda_entrada_verify = self.__moeda.pega_objeto(dados['nome_moeda_entrada'])
            moeda_saida_verify = self.__moeda.pega_objeto(dados['nome_moeda_saida'])
            corretos = True
            if pessoa_verify == None:
                NaoFoiEncontradoComEsteId(dados['id_pessoa'])
                corretos = False
            if moeda_entrada_verify == None:
                MoedaNaoEncontrada(dados['nome_moeda_entrada'])
                corretos = False
            if moeda_saida_verify == None:
                MoedaNaoEncontrada(dados['nome_moeda_saida'])
                corretos = False
            if not corretos:
                return
            dados['quantidade_saida'] = self.calculo_moeda_saida(dados['nome_moeda_entrada'], dados['nome_moeda_saida'], 
                                                                 dados['quantidade_entrada'], dados['juros'])
            trc = Troca(dados['id'], self.__cliente.pega_objeto(dados['id_pessoa']), 
                        dados['quantidade_entrada'], dados['quantidade_saida'], 
                        dados['data'], self.__moeda.pega_objeto(dados['nome_moeda_entrada']), 
                        self.__moeda.pega_objeto(dados['nome_moeda_saida']), dados['juros'])
            self.__trocas.add(trc)
            pessoa = self.__cliente.pega_objeto(dados['id_pessoa'])
            pessoa.trocas_feitas.append(trc)
            self.__relatorio.add_operacao('inclusao', f"Inclusao da Troca de id '{dados['id']}', realizada por '{pessoa.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            self.__tela.mostrar_msg(f"Troca de id '{dados['id']}' registrada com sucesso")


    def exclui(self):
        id = self.__tela.excluir()
        if id != None:
            troca = self.pega_objeto(id)
            if troca != None:
                self.__trocas.remove(troca.id)
                troca.pessoa.trocas_feitas.remove(troca)
                self.__tela.mostrar_msg(f"Troca de id '{id}' exluida com sucesso")
                self.__relatorio.add_operacao('exclusao', f"Exclusao da troca de id '{troca.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                NaoFoiEncontradoComEsteId('troca')

    def altera(self):
        id = self.__tela.alterar_dados()
        if id != None:
            troca = self.pega_objeto(id)
            if troca != None:
                new_dados = self.__tela.cadastrar_dados()
                troca.id = new_dados['id']
                troca.pessoa = self.__cliente.pega_objeto(new_dados['id_pessoa'])
                troca.quantidade_entrada = new_dados['quantidade_entrada']
                troca.quantidade_saida = self.calculo_moeda_saida(new_dados['nome_moeda_entrada'], new_dados['nome_moeda_saida'], 
                                                                new_dados['quantidade_entrada'], new_dados['juros'])
                troca.data = new_dados['data']
                troca.moeda_entrada = self.__moeda.pega_objeto(new_dados['nome_moeda_entrada'])
                troca.moeda_saida = self.__moeda.pega_objeto(new_dados['nome_moeda_saida'])
                troca.porcentagem_juros = new_dados['juros']
                self.__trocas.update(troca)
                self.__relatorio.add_operacao('alteracao', f"Alteracao de dados da troca de id '{troca.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                NaoFoiEncontradoComEsteId('troca')
    

    def mostra_todas(self):
        dados_trocas = []
        if self.__trocas.get_all() == []:
            NenhumRegistrado('troca')
        else:
            for troca in self.__trocas.get_all():
                dados_trocas.append({'id': troca.id, 'id_pessoa':troca.pessoa.id, 'data': troca.data, 
                                      'nome_moeda_entrada': troca.moeda_entrada.nome, 'nome_moeda_saida': troca.moeda_saida.nome, 
                                      'quantidade_entrada': troca.quantidade_entrada, 'quantidade_saida': troca.quantidade_saida, 
                                      'juros': troca.porcentagem_juros })
            self.__tela.mostrar_tabela(dados_trocas)
            self.__relatorio.add_operacao('mostragem', f"Mostragem dos dados de todas as trocas, {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            

    def calculo_moeda_saida(self, moeda1_nome, moeda2_nome, quantidade_entrada, juros):
        valor_entrada = self.__moeda.pega_objeto(moeda1_nome).valor_usd
        valor_saida = self.__moeda.pega_objeto(moeda2_nome).valor_usd
        valor_entrada_convertido = 1/valor_entrada
        valor_saida_convertido = 1/valor_saida
        valor_total = quantidade_entrada * valor_entrada_convertido
        valor_total -= valor_total* juros
        return round(valor_total/valor_saida_convertido, 2)
    

    def pega_objeto(self, id):
        if id != None:
            for troca in self.__trocas.get_all():
                if id == troca.id:
                    return troca
        

    def volta_tela(self):
        self.__controlador_sistema.abre_tela()
