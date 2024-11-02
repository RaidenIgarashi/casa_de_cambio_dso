from abstratas.absTela import Tela

class TelaEmprestimo(Tela):
    def tela_opcoes(self):
        print(f'-------EMPRESTIMO-------')
        print(f'1 - Registrar empréstimo')
        print(f'2 - Ver empréstimo registrado')
        print(f'3 - Excluir empréstimo')
        print(f'4 - Alterar empréstimo')
        print(f'5 - Listar todos empréstimos')
        print('0 - Retornar')

        opcoes = int(input("Escolha uma opção: "))
        return opcoes

    def cadastrar_dados(self):
        print('-------REGISTRANDO EMPRÉSTIMO--------')
        cliente = input('Digite o nome do cliente que pediu: ')
        emprestador = input('Digite o nome do emprestador: ')
        id = id
        quantidade_usd = input('Digite a quantidade que será repassada, em dólares: ')
        data = input('Digite a data em que foi feito o repasse [dd-mm-aa]: ')
        moeda = input('Digite o nome da moeda utilizada: ')
        juros_mensal = input('Digite a quantidade de juros mensal que será aplicado: ')
        emprestimo_pago = input('O empréstimo já foi devolvido? 0- não, 1- sim: ')
        return {'nome': nome, 'regioes': regioes, 'cifra': cifra, 'valor': valor}

    def mostrar_dados(self, dados_moeda):
        print('--------INFORMAÇÕES DA MOEDA--------')
        print(f'NOME: {dados_moeda["nome"]}')
        print(f'REGIOES: {dados_moeda["regioes"]}')
        print(f'CIFRA: {dados_moeda["cifra"]}')
        print(f'VALOR: {dados_moeda["valor"]}')
        print('\n')

    def excluir(self):
        nome = input('Escreva o nome da moeda que deseja excluir: ')
        return nome 

    def alterar_dados(self):
        nome = input('Escreva o nome da moeda que deseja alterar: ')
        return nome

    def ver_dados(self):
        nome = input('Escreva o nome da moeda que deseja achar: ')
        return nome

    def mostrar_msg(self, msg):
        print(msg)

    def mostrar_trocas(self):
        pass
