import PySimpleGUI as sg

class TelaRelatorio():    

    def relatorio_acoes(self, lista_operacao):
        titulo = ('INCLUSOES: ','ALTERACOES: ','EXCLUSOES: ','MOSTRAGENS: ','INDEFINIDOS: ',)
        nome = ('inclusão','alteração','exclusão','mostragem','indefinição',)
        for opr in range(len(lista_operacao)):
            if lista_operacao[opr] == []:
                if nome[opr] != 'indefinição':
                    self.mostra_msg(f'\nNenhuma {nome[opr]} foi registrada.\n', titulo[opr])
            else:
                self.mostra_acoes(lista_operacao[opr], titulo[opr])


    def mostra_acoes(self, msg_lst, titulo):
        soma_de_msg = ''
        for msg in msg_lst:
            soma_de_msg = soma_de_msg + msg + '\n\n'

        self.mostra_msg(soma_de_msg, f'--- AÇÕES DO USUÁRIO --- {titulo} ', )
        
        
        
    def mostra_cliente(self, infos):
        len_pessoas, len_organizacoes = infos['len_pessoas'], infos['len_org'], 
        maior_credito, menor_credito, mais_trans = infos['maior_credito'], infos['menor_credito'], infos['mais_trans']
        
        msg = f'''Quantidade de clientes registrados:   {len_pessoas + len_organizacoes-1}
Quantidade de Pessoas:   {len_pessoas}
Quantidade de Organizacoes:   {len_organizacoes-1}

Cliente com mais transacoes:  '{mais_trans[1]}' (id {mais_trans[2]}) com {mais_trans[0]} transações

Cliente com MAIOR crédito em empréstimos:  '{maior_credito[1]}' (id {maior_credito[2]}) com U$D {maior_credito[0]:.2f}
Cliente com MENOR crédito em empréstimos:  '{menor_credito[1]}' (id {menor_credito[2]}) com U$D {menor_credito[0]:.2f}'''
        
        self.mostra_msg(msg, 'CLIENTES')
        
        
        
    def mostra_moeda(self, infos):
        len_moedas, maior_valor, menor_valor = infos['len_moedas'], infos['maior_valor'], infos['menor_valor']
        
        msg = f'''Quantidade de moedas registradas:   {len_moedas}

Moeda com MAIOR valor em dólares:  '{maior_valor[1]}' com U$D {maior_valor[0]:.2f}
Moeda com MENOR valor em dólares:  '{menor_valor[1]}' com U$D {menor_valor[0]:.2f}'''
        
        self.mostra_msg(msg, 'MOEDAS')
        
        
        
    def mostra_troca(self, infos):
        len_trocas, maior_valor, menor_valor = infos['len_trocas'], infos['maior_valor'], infos['menor_valor']
        
        msg = f'''Quantidade de trocas registradas:   {len_trocas}
        
Troca de MAIOR valor:  '{maior_valor[1]}' feita por {maior_valor[2]} - U$D {maior_valor[0]:.2f}
Troca de MENOR valor:  '{menor_valor[1]}' feita por {menor_valor[2]} - U$D {menor_valor[0]:.2f}'''
        
        self.mostra_msg(msg, 'TROCAS')
        
        
        
    def mostra_emprestimo(self, infos):
        len_emprestimos, maior_valor, menor_valor, devolvidos = infos['len_emprestimos'], infos['maior_valor'], infos['menor_valor'], infos['devolvidos']
        
        msg = f'''Quantidade de emprestimos registradas:   {len_emprestimos}

Empréstimo de MAIOR valor:  '{maior_valor[1]}' de {maior_valor[2]} para {maior_valor[3]} | U$D {maior_valor[0]:.2f}
Empréstimo de MENOR valor:  '{menor_valor[1]}' de {menor_valor[2]} para {menor_valor[3]} | U$D {menor_valor[0]:.2f}
Porcentagem de empréstimos que já foram devolvidos: {100 * devolvidos/len_emprestimos}%'''
        self.mostra_msg(msg, 'EMPRÉSTIMOS')
        
        

    def mostra_msg(self, msg, titulo):
        sg.Popup(msg, title=titulo)
