from abstratas.absTela import Tela

class TelaMoeda(Tela):
    def tela_opcoes(self):
        print(f'-------MOEDAS-------')
        print(f'1 - Incluir moeda')
        print(f'2 - Excluir moeda')
        print(f'3 - Listar tudo de moedas')
        print(f'4 - Alterar moeda')
        print('0 - Retornar')

        opcoes = int(input("Escolha uma opção para ver/cadastrar: "))
        print()
        return opcoes

    def cadastrar_dados(self):
        print('-------CADASTRAR MOEDA--------')
        nome = input('Digite o nome da moeda: ')           #transforma as regioes em uma lista separando elas nas virgulas
        regioes = input('Digite uma ou mais regiões da moeda, separados por vírgula: ').split(',') 
        cifra = input('Digite a cifra da moeda: ')
        valor = input('Digite o valor em dólares da moeda: ')
        return {'nome': nome, 'regioes': regioes, 'cifra': cifra, 'valor': valor}

    def alterar_dados(self):
        pass

    def mostrar(self, dados_moeda):
        print('--------INFORMAÇÕES DA MOEDA--------')
        print(f'NOME: {dados_moeda["nome"]}')
        print(f'REGIOES: {dados_moeda["reg"]}')
        print(f'CIFRA: {dados_moeda["cifra"]}')
        print(f'VALOR: {dados_moeda["valor"]}')
        print('\n')

    def selecionar(self):
        nome = input('Escreva o nome da moeda que deseja achar')
        return nome

    def mostra_msg(msg):
        print(msg)

    def mostrar_trocas(self):
        pass
