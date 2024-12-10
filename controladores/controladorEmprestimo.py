from telas.telaEmprestimo import TelaEmprestimo
from entidades.emprestimo import Emprestimo
from abstratas.absControlador import Controlador
from funcoes import eh_pessoa
from excecoes import *
from datetime import datetime as dt
from DAOs.emprestimo_dao import EmprestimoDAO

class ControladorEmprestimo(Controlador):
    def __init__(self, controlador_sistema, controlador_moeda, controlador_cliente, relatorio):
        self.__controlador_sistema = controlador_sistema
        self.__relatorio = relatorio
        self.__emprestimos = EmprestimoDAO()
        self.__tela = TelaEmprestimo()
        self.__moeda = controlador_moeda
        self.__cliente = controlador_cliente
    
    def abre_tela(self):
        opcoes = {0: self.volta_tela, 1: self.mostra_dados, 2: self.inclui, 3: self.exclui, 
                      4: self.mostra_todas, 5: self.altera, 6: self.emprestimo_devolvido, 7: self.calcula_juros}
        while True:
            opcao_escolhida = self.__tela.init_opcoes()
            if opcao_escolhida == None:
                pass
            else:
                opcoes[opcao_escolhida]()  

    def inclui(self):
        dados = self.__tela.cadastrar_dados()
        if dados is not None:
            try:
                is_cliente = False
                cliente = self.__cliente.pega_objeto(dados['cliente_id'])
                emprestador = self.__cliente.pega_objeto(dados['emprestador_id'])
                moeda = self.__moeda.pega_objeto(dados['moeda'])
                if cliente is None:
                    is_cliente = True
                    raise ValueError(dados['cliente_id'])
                if emprestador is None:
                    is_cliente = True
                    raise ValueError(dados['emprestador_id'])
                if moeda is None:
                    raise ValueError(dados['moeda'])
            except ValueError as e:
                self.__tela.mostrar_dados()
                if is_cliente:
                    raise NaoFoiEncontradoComEsteId('cliente')
                else:
                    raise MoedaNaoEncontrada
            emp = Emprestimo(dados['id'], cliente, emprestador, moeda, dados['quantia_repassada'], 
                             dados['data_do_repasse'], dados['data_pretendida'], dados['juros_normal'], 
                             dados['juros_mensal_atraso'], dados['devolvido'], dados['data_devolvida'])
            self.__emprestimos.add(emp)
            emp.cliente.emprestimos_pedidos.append(emp)
            emp.emprestador.emprestimos_concedidos.append(emp)
            self.__tela.mostrar_msg(f'Emprestimo de id {dados['id']} adicionado com sucesso')
            self.__relatorio.add_operacao('inclusao', f"Inclusao do Emprestimo de id '{dados['id']}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")


    def calcula_juros(self):
        pass
    #     id = self.__tela.ver_juros()
    #     emp = self.pega_objeto(id)
    #     if emp is None:
    #         raise NaoFoiEncontradoComEsteId('emprestimo')
    #     else:
    #         if emp.devolvido == True:
    #             data = emp.data_devolvida
    #             info = ['(Empréstimo já devolvido)', 'tinha']
    #         else:
    #             data = self.__tela.escolher_data()
    #             data = dt.strptime(data, '%d/%m/%Y')
    #             info = ['(Data escolhida)', 'teria']
    #         juros = emp.devolucao.calcula_juros(data)
    #         return(f'Na data {data}, o empréstimo de id {id} {info[1]} um acúmulo \
    #                total de {emp.moeda.cifra}{juros} em juros | {info[0]}')
        

    def emprestimo_devolvido(self):
        dados = self.__tela.emprestimo_devolvido()
        id = dados['id']
        data = dados['data']
        existe = False
        for emp in self.__emprestimos.get_all():
            if id == emp.id:
                if emp.devolvido == True:
                    self.__tela.mostrar_dados(f'## empréstimo já devolvido em {emp.data_devolvida}##')
                else:
                    emp.devolvido = True
                    emp.data_devolvida = data
                    self.__relatorio.add_operacao('alteracao', f"Emprestimo de id '{emp.id}' registrado como devolvido na data {emp.data_devolvida}; registro feito {dt.now().strftime('dia %d/%m/%Y, às %H:%M')}")
                existe = True
        if not existe:
            raise NaoFoiEncontradoComEsteId('emprestimo')

    def mostra_dados(self):
        id = self.__tela.ver_dados()
        emp = self.pega_objeto(id)
        if emp is None:
            raise NaoFoiEncontradoComEsteId('emprestimo')
        else:
            self.__tela.mostrar_dados([{'id':emp.id, 'cliente_id':emp.cliente.id, 'emprestador_id':emp.emprestador.id, 
                                       'moeda':emp.moeda, 'quantia_repassada':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                       'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                       'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido}])
            self.__relatorio.add_operacao('mostragem', f"Mostragem de dados do Empréstimo '{emp.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")

    def pega_objeto(self, id):
        for emp in self.__emprestimos.get_all():
            if id == emp.id:
                return emp
        return None

    def exclui(self):
        id = self.__tela.excluir()
        emprestimo = self.pega_objeto(id)
        if emprestimo != None:
            self.__emprestimos.remove(emprestimo.id)
            emprestimo.cliente.emprestimos_pedidos.remove(emprestimo)
            emprestimo.emprestador.emprestimos_concedidos.remove(emprestimo)
            self.__relatorio.add_operacao('exclusao', f"Exclusão do Empréstimo '{emprestimo.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
            self.__tela.mostrar_msg(f"\n# Exclusão do empréstimo {emprestimo.nome} feita com sucesso #\n")
        else:
            raise NaoFoiEncontradoComEsteId('emprestimo')

    def altera(self):
        id = self.__tela.alterar_dados()
        emp = self.pega_objeto(id)
        if emp != None:
            novos_dados = self.__tela.cadastrar_dados()
            nomes = ['id', 'cliente', 'emprestador', 'moeda', 'quantia_repassada', 'data_do_repasse', 
                     'data_devolvida', 'data_pretendida', 'juros_normal', 'juros_mensal_atraso', 'devolvido']

            dados_alterar = [emp.id, emp.cliente.id, emp.emprestador.id, emp.moeda, emp.quantia_repassada, emp.data_do_repasse, 
                     emp.data_devolvida, emp.data_pretendida, emp.juros_normal, emp.juros_mensal_atraso, emp.devolvido]
            for d in range(len(dados_alterar)):
                dados_alterar[d] = novos_dados[nomes[d]]
            self.__relatorio.add_operacao('alteracao', f"Alteracao de dados do Empréstimo '{emp.id}', {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")
        else:
            raise NaoFoiEncontradoComEsteId('emprestimo')

    def mostra_todas(self):
        if len(self.__emprestimos.get_all()) == 0:
            raise NenhumRegistrado('empréstimo')
        else:
            for emp in self.__emprestimos.get_all():
                self.__tela.mostrar_dados([{'id':emp.id, 'cliente_id':emp.cliente.id, 'emprestador_id':emp.emprestador.id, 
                                       'moeda':emp.moeda.nome, 'quantia_repassada':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                       'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                       'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido}])
            self.__relatorio.add_operacao('mostragem', f"Mostragem de todos os empréstimos registrados, {dt.now().strftime('Dia %d/%m/%Y, às %H:%M')}")

    def volta_tela(self):
        self.__controlador_sistema.abre_tela()

