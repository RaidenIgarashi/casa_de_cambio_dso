from abstratas.absTela import Tela

class TelaMoeda(Tela):
    def tela_opcoes(self):
        print('-------CLIENTES-------')
        print('1 - Incluir moeda')
        print('2 - Excluir moeda')
        print('3 - Listar todos moedas')
        print('4 - Alterar moeda')
        print('0 - Retornar')

        opcoes = int(input("Escolha uma opção para ver/cadastrar: "))
        return opcoes

    def cadastrar_dados(self, id):
        print('-------CADASTRAR MOEDA--------')
        nome = input('Digite o nome dá moeda')
        reg = input('Digite de onde veio')
        cifra = input('Digite a cifra da moeda')
        valor = input('Digite o valor da moeda')
        return {'nome': nome, 'reg': reg, 'cifra': cifra, 'valor': valor}

    def alterar_dados(self):
        pass

    def mostrar(self, dados_moeda):
        print('--------INFORMAÇÕES DA MOEDA--------')
        print(f'NOME: {dados_moeda['nome']}')
        print(f'ORIGEM: {dados_moeda['reg']}')
        print(f'CIFRA: {dados_moeda['cifra']}')
        print(f'VALOR: {dados_moeda['valor']}')
        print('\n')

    def selecionar(self):
        pass

    def mostra_msg(self):
        pass

    def mostrar_trocas(self):
        pass
