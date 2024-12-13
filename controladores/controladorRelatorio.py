from telas.telaRelatorio import TelaRelatorio
from entidades.pessoa import Pessoa

class Relatorio():
    def __init__(self, cont_sistema, cont_cliente, cont_moeda, cont_troca, cont_emprestimo):
        self.__cont_sistema = cont_sistema
        self.__cont_cliente = cont_cliente
        self.__cont_moeda = cont_moeda
        self.__cont_troca = cont_troca
        self.__cont_emprestimo = cont_emprestimo
        self.__tela = TelaRelatorio()
        
            
    def relatorio_acoes_usuario(self):
        lista_operacao = (self.__cont_sistema.inclusoes, self.__cont_sistema.alteracoes, self.__cont_sistema.exclusoes,
                          self.__cont_sistema.mostragens, self.__cont_sistema.indefinidos)
        self.__tela.relatorio_acoes(lista_operacao)  
                  
            
    def relatorio_clientes(self):
        self.__cont_cliente.mostra_todas()
        
        pessoas = self.__cont_cliente.pessoas.get_all()
        organizacoes = self.__cont_cliente.organizacoes.get_all()

        for c, cli in enumerate(list(pessoas) + list(organizacoes)):
            qnt_transacoes = len(cli.emprestimos_pedidos) + len(cli.emprestimos_concedidos) 
            if isinstance(cli, Pessoa):
               qnt_transacoes += len(cli.trocas_feitas)
            if c == 0:
                mais_trans = [qnt_transacoes, cli.nome, cli.id]
            elif qnt_transacoes > mais_trans[0]:
                mais_trans = [qnt_transacoes, cli.nome, cli.id]
            
            credito_pos, credito_neg = 0, 0
            for emp in cli.emprestimos_pedidos: 
                credito_neg += emp.quantia_repassada
            for emp in cli.emprestimos_concedidos: 
                credito_pos += emp.quantia_repassada
            credito = credito_pos - credito_neg
            
            if c == 0:
                maior_credito = (credito, cli.nome, cli.id)
                menor_credito = (credito, cli.nome, cli.id)
            elif credito > maior_credito[0]:
                maior_credito = (credito, cli.nome, cli.id)
            elif credito < menor_credito[0]:
                menor_credito = (credito, cli.nome, cli.id) 
             
        msg = f'''Quantidade de clientes registrados:   {len(pessoas) + len(organizacoes)-1}
Quantidade de Pessoas:   {len(pessoas)}
Quantidade de Organizacoes:   {len(organizacoes)-1}'''

# Cliente com mais transacoes:  '{mais_trans[1]}' (id {mais_trans[2]}) com {mais_trans[0]} transações

# Cliente com MAIOR crédito em empréstimos:  '{maior_credito[1]}' (id {maior_credito[2]}) com U$D {maior_credito[0]:.2f}
# Cliente com MENOR crédito em empréstimos:  '{menor_credito[1]}' (id {menor_credito[2]}) com U$D {menor_credito[0]:.2f}'''
        
        self.__tela.mostra_msg(msg, 'CLIENTES')
        
    
    def relatorio_moedas(self):
        self.__cont_moeda.mostra_todas()
        
        moedas = self.__cont_moeda.moedas.get_all()
        
        maior_valor, menor_valor = (1, 'Dolar'), (1, 'Dolar')
        for m in moedas:
            valor = m.valor_usd
            if valor > maior_valor[0]:
                maior_valor = (valor, m.nome)
            elif valor < menor_valor[0]:
                menor_valor = (valor, m.nome)
            
        msg = f'''Quantidade de moedas registradas:   {len(moedas)}

Moeda com MAIOR valor em dólares:  '{maior_valor[1]}' com U$D {maior_valor[0]:.2f}
Moeda com MENOR valor em dólares:  '{menor_valor[1]}' com U$D {menor_valor[0]:.2f}'''
        
        self.__tela.mostra_msg(msg, 'MOEDAS')
        
    
    def relatorio_trocas(self):
        self.__cont_troca.mostra_todas()
        
        trocas = self.__cont_troca.trocas.get_all()
        
        for c, t in enumerate(trocas):
            valor = t.quantidade_entrada * t.moeda_entrada.valor_usd
            if c == 0:
                maior_valor = (valor, t.id, t.pessoa.nome)
                menor_valor = (valor, t.id, t.pessoa.nome)
            elif valor > maior_valor[0]:
                maior_valor = (valor, t.id, t.pessoa.nome)
            elif valor < menor_valor[0]:
                menor_valor = (valor, t.id, t.pessoa.nome) 
            
        msg = f'''Quantidade de trocas registradas:   {len(trocas)}

Troca de MAIOR valor:  '{maior_valor[1]}' feita por {maior_valor[2]} - U$D {maior_valor[0]:.2f}
Troca de MENOR valor:  '{menor_valor[1]}' feita por {menor_valor[2]} - U$D {menor_valor[0]:.2f}'''
        
        self.__tela.mostra_msg(msg, 'TROCAS')
        
    
    def relatorio_emprestimos(self):
        self.__cont_emprestimo.mostra_todas()
        
        emprestimos = self.__cont_emprestimo.emprestimos.get_all()
        
        devolvidos = 0
        for c, emp in enumerate(emprestimos):
            valor = emp.quantia_repassada
            if c == 0:
                maior_valor = (valor, emp.id, emp.emprestador.nome, emp.cliente.nome)
                menor_valor = (valor, emp.id, emp.emprestador.nome, emp.cliente.nome)
            elif valor > maior_valor[0]:
                maior_valor = (valor, emp.id, emp.emprestador.nome, emp.cliente.nome)
            elif valor < menor_valor[0]:
                menor_valor = (valor, emp.id, emp.emprestador.nome, emp.cliente.nome) 
            if emp.devolvido:
                devolvidos += 1
            
        msg = f'''Quantidade de emprestimos registradas:   {len(emprestimos)}

Empréstimo de MAIOR valor:  '{maior_valor[1]}' de {maior_valor[2]} para {maior_valor[3]} | U$D {maior_valor[0]:.2f}
Empréstimo de MENOR valor:  '{menor_valor[1]}' de {menor_valor[2]} para {menor_valor[3]} | U$D {menor_valor[0]:.2f}
Porcentagem de empréstimos que já foram devolvidos: {100 * devolvidos/len(emprestimos)}%'''
        self.__tela.mostra_msg(msg, 'EMPRÉSTIMOS')
            
            
    def gera_relatorio(self):
        self.relatorio_clientes()
        self.relatorio_moedas()
        self.relatorio_trocas()
        self.relatorio_emprestimos()
         
