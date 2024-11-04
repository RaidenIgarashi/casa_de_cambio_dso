from telas.telaEmprestimo import TelaEmprestimo
from entidades.emprestimo import Emprestimo
from abstratas.absControlador import Controlador
from controladores.funcoes import eh_pessoa

class ControladorEmprestimo(Controlador):
    def __init__(self, controlador_sistema, controlador_moeda, controlador_cliente):
        self.__controlador_sistema = controlador_sistema
        self.__emprestimos = []
        self.__tela = TelaEmprestimo()
        self.__moeda = controlador_moeda
        self.__cliente = controlador_cliente
        

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
                print()
                if is_cliente:
                    print(f'Não existe cliente com identidade "{e}" registrado')
                else:
                    print(f'A moeda "{e}" não está registrada')
                print()
                return
            emp = Emprestimo(dados['id'], cliente, emprestador, moeda, dados['quantia'], 
                             dados['data_do_repasse'], dados['data_pretendida'], dados['juros_normal'], 
                             dados['juros_mensal_atraso'], dados['devolvido'], dados['data_devolvida'])
            self.__emprestimos.append(emp)
            emp.cliente.emprestimos_pedidos = emp
            emp.emprestador.emprestimos_concedidos = emp


    def calcula_juros(self):
        id = self.__tela.ver_juros()
        emp = self.pega_objeto(id)
        if emp is None:
            print()
            print('## não foi encontrado empréstimo com esse ID ##')
            print()
        else:
            if emp.devolvido == True:
                data = emp.data_devolvida
                info = ['(Empréstimo já devolvido)', 'tinha']
            else:
                data = self.__tela.escolher_data
                info = ['(Data escolhida)', 'teria']
            juros = emp.devolucao.calcula_juros(data)
            return(f'Na data {data}, o empréstimo de id {id} {info[1]} um acúmulo \
                   total de {emp.moeda.cifra}{juros} em juros | {info[0]}')
        

    def emprestimo_devolvido(self):
        dados = self.__tela.emprestimo_devolvido()
        id = dados['id']
        data = dados['data']
        existe = False
        for emp in self.__emprestimos:
            if id == emp.id:
                if emp.devolvido == True:
                    print(f'## empréstimo já devolvido em {emp.data_devolvida}##')
                else:
                    emp.devolvido = True
                    emp.data_devolvida = data
                existe = True
        if not existe:
            print()
            print('## não foi encontrado empréstimo com esse ID ##')
            print()

    def mostra_dados(self):
        id = self.__tela.ver_dados()
        emp = self.pega_objeto(id)
        if emp is None:
            print()
            print('## não foi encontrado empréstimo com esse ID ##')
            print()
        else:
            cliente_id = emp.cliente.cpf if eh_pessoa(emp.cliente) else emp.cliente.cnpj
            emp_id = emp.emprestador.cpf if eh_pessoa(emp.emprestador) else emp.emprestador.cnpj
            self.__tela.mostrar_dados({'id':emp.id, 'cliente_id':cliente_id, 'emprestador_id':emp_id, 
                                       'moeda':emp.moeda, 'quantia':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                       'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                       'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido})

    def pega_objeto(self, id):
        for emp in self.__emprestimos:
            if id == emp.id:
                return emp
        return None
        

    def exclui(self):
        id = self.__tela.excluir()
        emprestimo = self.pega_objeto(id)
        if emprestimo != None:
            self.__emprestimos.remove(emprestimo)
            emprestimo.cliente.emprestimos_pedidos_remove(emprestimo)
            emprestimo.emprestador.emprestimos_concedidos_remove(emprestimo)
            
        else:
            print()
            print('## não foi encontrado empréstimo com esse ID ##')
            print()

    def altera(self):
        id = self.__tela.alterar_dados()
        emp = self.pega_objeto(id)
        if emp != None:
            novos_dados = self.__tela.cadastrar_dados()
            nomes = ['id', 'cliente_id', 'emprestador_id', 'moeda', 'quantia', 'data_do_repasse', 
                     'data_devolvida', 'data_pretendida', 'juros_normal', 'juros_mensal_atraso', 'devolvido']
            
            cliente_id = emp.cliente.cpf if eh_pessoa(emp.cliente) else emp.cliente.cnpj
            emp_id = emp.emprestador.cpf if eh_pessoa(emp.emprestador) else emp.emprestador.cnpj

            dados_alterar = [emp.id, emp.cliente, emp.emprestador, emp.moeda, emp.quantia_repassada, emp.data_do_repasse, 
                     emp.data_devolvida, emp.data_pretendida, emp.juros_normal, emp.juros_mensal_atraso, emp.devolvido]
            for d in range(len(dados_alterar)):
                dados_alterar[d] = novos_dados[nomes[d]]

        else:
            print()
            print('## não foi encontrado empréstimo com esse ID ##')
            print()

    def mostra_todas(self):
        if len(self.__emprestimos) == 0:
            print()
            print('## Nenhum empréstimo registrado ##')
            print()
        else:
            for emp in self.__emprestimos:
                cliente_id = emp.cliente.cpf if eh_pessoa(emp.cliente) else emp.cliente.cnpj
                emp_id = emp.emprestador.cpf if eh_pessoa(emp.emprestador) else emp.emprestador.cnpj
                self.__tela.mostrar_dados({'id':emp.id, 'cliente_id':cliente_id, 'emprestador_id':emp_id, 
                                       'moeda':emp.moeda, 'quantia':emp.quantia_repassada, 'data_do_repasse':emp.data_do_repasse, 
                                       'data_devolvida':emp.data_devolvida, 'data_pretendida':emp.data_pretendida, 
                                       'juros_normal':emp.juros_normal, 'juros_mensal_atraso':emp.juros_mensal_atraso, 'devolvido': emp.devolvido})
    
    def abre_tela(self):
        commandlst = {0: self.volta_tela, 1: self.inclui, 2: self.mostra_dados, 3: self.exclui, 
                      4: self.altera, 5: self.emprestimo_devolvido, 6: self.mostra_todas, 7: self.calcula_juros}
        
        while True:
            commandlst[self.__tela.tela_opcoes()]()

    def volta_tela(self):
        self.__controlador_sistema.abre_tela()

