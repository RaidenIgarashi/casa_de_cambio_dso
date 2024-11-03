from abstratas.absTela import Tela

class TelaMoeda(Tela):
    def tela_opcoes(self):
        print(f'-------MOEDAS-------')
        print(f'1 - Ver dados de uma Moeda')
        print(f'2 - Incluir moeda')
        print(f'3 - Excluir moeda')
        print(f'4 - Listar tudo de moedas')
        print(f'5 - Alterar moeda')
        print('0 - Retornar')

        opcoes = int(input("Escolha uma opção para ver/cadastrar: "))
        print()
        return opcoes

    def cadastrar_dados(self):
        print('-------CADASTRAR MOEDA--------')
        nome = input('Digite o nome da moeda: ')           #transforma as regioes em uma lista separando elas nas virgulas
        regioes = input('Digite uma ou mais regiões da moeda, separados por vírgula: ').split(',') 
        cifra = input('Digite a cifra da moeda: ')
        try:
            valor = float(input('Digite o valor em dólares da moeda: '))
        except:
            print()
            print('## isso não é um valor')
            print()
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
