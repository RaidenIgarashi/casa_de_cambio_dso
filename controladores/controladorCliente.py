from abstratas.absControlador import Controlador
from telas.telaCliente import TelaCliente
from telas.telaEmprestimo import TelaEmprestimo
from telas.telaTroca import TelaTroca
from entidades.organizacao import Organizacao
from entidades.pessoa import Pessoa
from funcoes import eh_pessoa
from excecoes import *
from datetime import datetime as dt
from DAOs.pessoa_dao import PessoaDAO
from DAOs.organizacao_dao import OrganizacaoDAO

class ControladorCliente(Controlador):
    def __init__(self, controlador_sistema, relatorio):
        self.__controlador_sistema = controlador_sistema
        self.__relatorio = relatorio
        self.__tela = TelaCliente()
        self.__tela_emprestimo = TelaEmprestimo()
        self.__tela_troca = TelaTroca()
        self.__pessoas = PessoaDAO()
        self.__organizacoes = OrganizacaoDAO()

    def abre_tela(self):
        opcoes = {1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 4: self.mostra_todas, 
                  5: self.altera, 6: self.mostra_transacoes, 0: self.voltar_tela}
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  
                
    def inclui(self):
        dados_cliente = self.__tela.cadastrar_dados()
        if dados_cliente is not None:   # se nada for digitado incorretamente
            if 'idade' in dados_cliente: 
                self.__pessoas.add(Pessoa(dados_cliente['nome'], dados_cliente['id'], dados_cliente['idade']))
                #self.__pessoas.append(Pessoa(dados_cliente['nome'], dados_cliente['id'], dados_cliente['idade']))
            else:
                self.__organizacoes.add(Organizacao(dados_cliente['nome'], dados_cliente['id']))
            self.__tela.mostrar_msg(f"Cliente '{dados_cliente['nome']}' adicionado com sucesso")
            self.__relatorio.add_operacao('inclusao', f"Inclusao do Cliente '{dados_cliente['nome']}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
                

    def mostra_dados(self):
        id = self.__tela.ver_dados()
        existente = False
        if id != None:  # se o id nao for digitado incorretamente
            for pessoa in self.__pessoas.get_all():
                if pessoa.id == id:
                    self.__tela.mostrar_tabela([{'nome': pessoa.nome, 'id': pessoa.id, 'idade':pessoa.idade}], 1)
                    existente = True
                    self.__relatorio.add_operacao('mostragem', f"Mostragem de dados do Cliente '{pessoa.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            for org in self.__organizacoes.get_all():
                if org.id == id:
                    self.__tela.mostrar_tabela([{'nome': org.nome, 'id': org.id}], 0)
                    existente = True
                    self.__relatorio.add_operacao('mostragem', f"Mostragem de dados do Cliente '{org.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            if not existente:
                raise NaoFoiEncontradoComEsteId('cliente')


    def exclui(self):
        id = self.__tela.excluir()
        cliente = self.pega_objeto(id)
        if id != None:   # se o id nao for digitado incorretamente
            if cliente != None: # se o cliente existir
                if eh_pessoa(id):
                    self.__pessoas.remove(cliente.id)
                else:
                    self.__organizacoes.remove(cliente.id)
                self.__tela.mostrar_msg(f'Cliente "{cliente.nome}" excluído.')
                self.__relatorio.add_operacao('exclusao', f"Exclusão do Cliente '{cliente.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                raise NaoFoiEncontradoComEsteId('cliente')
            

    def mostra_todas(self):
        dados_pessoa = []
        dados_org = []
        if len(self.__organizacoes.get_all()) > 0:
            for org in self.__organizacoes.get_all():
                dados_org.append({'nome': org.nome, 'id': org.id, 'idade': ''})
            self.__tela.mostrar_tabela(dados_org, 0)
        else:
            self.__tela.mostrar_msg("Nenhuma Organização cadastrada.\n")

        if len(self.__pessoas.get_all()) > 0:
            for pessoa in self.__pessoas.get_all():
                dados_pessoa.append({'nome': pessoa.nome, 'id': pessoa.id, 'idade': pessoa.idade})
            self.__tela.mostrar_tabela(dados_pessoa, 1)
        else:
            self.__tela.mostrar_msg("Nenhuma Pessoa cadastrada.\n")
        self.__relatorio.add_operacao('mostragem', f"Mostragem de todos as Pessoas e Organizacoes registradas, {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
        

    def altera(self):
        id = self.__tela.alterar_dados()
        id_a_alterar = self.pega_objeto(id)
        if id != None:   # se o id nao for digitado incorretamente
            if id_a_alterar != None:  # se o id estiver registrado
                lista = self.__pessoas.get_all() if eh_pessoa(id) else self.__organizacoes.get_all()
                for cliente in lista:
                    if cliente.id == id_a_alterar.id:
                        novo_cliente = self.__tela.cadastrar_dados()
                        cliente.nome = novo_cliente['nome']
                        cliente.id = novo_cliente['id']
                        if len(id) == 3:
                            cliente.idade = novo_cliente['idade']
                self.__relatorio.add_operacao('alteracao', f"Alteracao dos dados do Cliente '{cliente.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                raise NaoFoiEncontradoComEsteId('cliente')
            
    
    def mostra_transacoes(self):
        id = self.__tela.ver_dados()
        existente = False
        eh_pes = eh_pessoa(id)
        if eh_pes == True: # se for cpf
            for pessoa in self.__pessoas.get_all():
                if pessoa.id == id:
                    cliente = pessoa
                    existente = True
        elif eh_pes == False: # se for cnpj
            for org in self.__organizacoes.get_all():
                if org.id == id:
                    cliente = org
                    existente = True
        if existente:
            if len(cliente.emprestimos_pedidos) > 0:
                self.__tela_emprestimo.mostrar_msg('\n- EMPRESTIMOS PEDIDOS: \n')
                for t in cliente.emprestimos_pedidos:
                    self.__tela_emprestimo.mostrar_tabela({'id':t.id, 'cliente_id':t.cliente.id, 'emprestador_id':t.emprestador.id, 'moeda':t.moeda, 'quantia_repassada':t.quantia_repassada, 
                                                         'data_do_repasse':t.data_do_repasse, 'devolvido':t.devolvido, 'data_devolvida':t.data_devolvida, 'data_pretendida':t.data_pretendida, 
                                                         'juros_normal':t.juros_normal, 'juros_mensal_atraso':t.juros_mensal_atraso})
            else:
                self.__tela_emprestimo.mostrar_msg('\nEste cliente não pediu nenhum empréstimo. \n')

            if len(cliente.emprestimos_concedidos) > 0:
                self.__tela_emprestimo.mostrar_msg('\n- EMPRESTIMOS CONCEDIDOS: \n')
                for t in cliente.emprestimos_concedidos:
                    self.__tela_emprestimo.mostrar_tabela({'id':t.id, 'cliente_id':t.cliente.id, 'emprestador_id':t.emprestador.id, 'moeda':t.moeda, 'quantia_repassada':t.quantia_repassada, 
                                                         'data_do_repasse':t.data_do_repasse, 'devolvido':t.devolvido, 'data_devolvida':t.data_devolvida, 'data_pretendida':t.data_pretendida, 
                                                         'juros_normal':t.juros_normal, 'juros_mensal_atraso':t.juros_mensal_atraso})
            else:
                self.__tela_emprestimo.mostrar_msg('\nEste cliente não concedeu empréstimos a ninguém. \n')

            if eh_pes:
                if len(cliente.trocas_feitas) > 0:
                    self.__tela_emprestimo.mostrar_tabela('\n- TROCAS CAMBIAIS FEITAS: \n')
                    for t in cliente.trocas_feitas:
                        self.__tela_troca.mostrar_tabela({'id': t.id, 'id_pessoa':cliente.id, 'data': t.data, 
                                                        'moeda_entrada': t.moeda_entrada, 'moeda_saida': t.moeda_saida, 
                                                        'quantidade_entrada': t.quantidade_entrada, 'quantidade_saida': t.quantidade_saida, 
                                                        'juros': t.porcentagem_juros})   
                else:
                    self.__tela_emprestimo.mostrar_msg('\nEste cliente não fez nenhuma troca cambial. \n')
            self.__relatorio.add_operacao('mostragem', f"Mostragem de todas as transações do cliente '{cliente.nome}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
        elif eh_pes != None:
            raise NenhumRegistrado('cliente')
            
    def pega_objeto(self, id):  # funcao interna
        if id != None:
            for cli in self.__pessoas.get_all():
                if cli.id == id:
                    return cli 
            for cli in self.__organizacoes.get_all():
                if cli.id == id:
                    return cli


    def voltar_tela(self):
        self.__controlador_sistema.abre_tela()
