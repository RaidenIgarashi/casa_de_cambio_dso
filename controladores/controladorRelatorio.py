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
             
        self.__tela.mostra_cliente({'len_pessoas':len(pessoas), 'len_org':len(organizacoes), 
                                    'maior_credito':maior_credito, 'menor_credito':menor_credito, 'mais_trans':mais_trans})
        
    
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
            
        self.__tela.mostra_moeda({'len_moedas':len(moedas), 'maior_valor':maior_valor, 'menor_valor':menor_valor})
        
    
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
            
        self.__tela.mostra_troca({'len_trocas':len(trocas), 'maior_valor':maior_valor, 'menor_valor':menor_valor})
        
    
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

        self.__tela.mostra_emprestimo({'len_emprestimos':len(emprestimos), 'maior_valor':maior_valor, 'menor_valor':menor_valor, 'devolvidos':devolvidos})
            
            
    def gera_relatorio(self):
        self.relatorio_clientes()
        self.relatorio_moedas()
        self.relatorio_trocas()
        self.relatorio_emprestimos()
         
