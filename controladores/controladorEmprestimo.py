from telas.telaEmprestimo import TelaEmprestimo
from entidades.emprestimo import Emprestimo
from abstratas.absControlador import Controlador
from funcoes import eh_pessoa
from excecoes import *
from datetime import datetime as dt
from DAOs.emprestimo_dao import EmprestimoDAO

class ControladorEmprestimo(Controlador):
    def __init__(self, controlador_sistema, controlador_moeda, controlador_cliente):
        self.__controlador_sistema = controlador_sistema
        self.__emprestimos = EmprestimoDAO()
        self.__tela = TelaEmprestimo()
        self.__moeda = controlador_moeda
        self.__cliente = controlador_cliente
        
    @property
    def emprestimos(self):
        return self.__emprestimos
    
    def abre_tela(self):
        opcoes = {0: self.volta_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 
                      4: self.mostra_todas, 5: self.altera, 6: self.emprestimo_devolvido, 7: self.calcula_juros}
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  
                
    def pega_objeto(self, id):
        if id != None:
            for emp in self.__emprestimos.get_all():
                if id == emp.id:
                    return emp

    def volta_tela(self):
        self.__controlador_sistema.abre_tela()
                
                
    def mostra_dados(self):
        id = self.__tela.ver_dados()
        if id != None:
            emp = self.pega_objeto(id)
            if emp is None:
                NaoFoiEncontradoComEsteId('emprestimo')
            else:
                self.__tela.mostrar_tabela([{'id':emp.id, 'cliente_id':emp.cliente.id, 'emprestador_id':emp.emprestador.id, 
                                        'moeda':emp.moeda, 'quantia_repassada':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                        'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                        'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido}])
                self.__controlador_sistema.add_operacao('mostragem', f"Mostragem de dados do Empréstimo '{emp.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
                

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        if dados != None:
            corretos = True
            cliente = self.__cliente.pega_objeto(dados['cliente_id'])
            emprestador = self.__cliente.pega_objeto(dados['emprestador_id'])
            moeda = self.__moeda.pega_objeto(dados['moeda'])
            if cliente == None:
                corretos = False
                ValueError(dados['cliente_id'])
            if emprestador == None:
                corretos = False
                ValueError(dados['emprestador_id'])
            if moeda == None:
                corretos = False
                ValueError(dados['moeda'])
            if not corretos:
                return
            
            emp = Emprestimo(dados['id'], cliente, emprestador, moeda, dados['quantia_repassada'], 
                             dados['data_do_repasse'], dados['data_pretendida'], dados['juros_normal'], 
                             dados['juros_mensal_atraso'], dados['devolvido'], dados['data_devolvida'])
            self.__emprestimos.add(emp)
            emp.cliente.emprestimos_pedidos.append(emp)
            emp.emprestador.emprestimos_concedidos.append(emp)
            self.__tela.mostrar_msg(f'Emprestimo de id {dados['id']} adicionado com sucesso')
            self.__controlador_sistema.add_operacao('inclusao', f"Inclusao do Emprestimo de id '{dados['id']}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            
            
    def exclui(self):
        id = self.__tela.excluir()
        if id != None:
            emprestimo = self.pega_objeto(id)
            if emprestimo != None:
                self.__emprestimos.remove(emprestimo.id)
                self.__controlador_sistema.add_operacao('exclusao', f"Exclusão do Empréstimo '{emprestimo.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
                self.__tela.mostrar_msg(f"\n# Exclusão do empréstimo {emprestimo.id} feita com sucesso #\n")
            else:
                NaoFoiEncontradoComEsteId('emprestimo')
            

    def altera(self):
        id = self.__tela.alterar_dados()
        if id != None:
            emp = self.pega_objeto(id)
            if emp != None:
                novos_dados = self.__tela.cadastrar_dados()
                emp = Emprestimo(novos_dados['id'], self.__cliente.pega_objeto(novos_dados['cliente_id']), self.__cliente.pega_objeto(novos_dados['emprestador_id']), 
                                 self.__moeda.pega_objeto(novos_dados['moeda']), novos_dados['quantia_repassada'], novos_dados['data_do_repasse'], 
                                 novos_dados['data_pretendida'], novos_dados['juros_normal'], novos_dados['juros_mensal_atraso'], 
                                 novos_dados['devolvido'], novos_dados['data_devolvida'])

                self.__emprestimos.update(emp)
                self.__tela.mostrar_msg(f'Emprestimo "{novos_dados['id']}" alterado com sucesso.')
                self.__controlador_sistema.add_operacao('alteracao', f"Alteracao de dados do Empréstimo '{emp.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            else:
                NaoFoiEncontradoComEsteId('emprestimo')
    
    
    def mostra_todas(self):
        dados_emprestimos = []
        if len(self.__emprestimos.get_all()) == 0:
            NenhumRegistrado('empréstimo')
        else:
            for emp in self.__emprestimos.get_all():
                dados_emprestimos.append({'id':emp.id, 'cliente_id':emp.cliente.id, 'emprestador_id':emp.emprestador.id, 
                                       'moeda':emp.moeda.nome, 'quantia_repassada':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                       'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                       'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido})
            self.__tela.mostrar_tabela(dados_emprestimos)
            self.__controlador_sistema.add_operacao('mostragem', f"Mostragem de todos os empréstimos registrados, {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")


    def emprestimo_devolvido(self):
        dados = self.__tela.emprestimo_devolvido()
        if dados != None:
            id = dados['id']
            data = dados['data']
            existe = False
            for emp in self.__emprestimos.get_all():
                if id == emp.id:
                    if emp.devolvido == True:
                        self.__tela.mostrar_msg(f'## empréstimo já devolvido em {emp.data_devolvida}##')
                    else:
                        emp.devolvido = True
                        emp.data_devolvida = data
                        self.__emprestimos.update(emp)
                        self.__tela.mostrar_msg(f'Devolucao do emprestimo de id {id} registrada - data: {data}')
                        self.__controlador_sistema.add_operacao('alteracao', f"Emprestimo de id '{emp.id}' registrado como devolvido na data {emp.data_devolvida}; registro feito {dt.now().strftime('dia %d/%m/%Y, às %H:%M')}")
                    existe = True
            if not existe:
                NaoFoiEncontradoComEsteId('emprestimo')
                 

    def calcula_juros(self):
        pass