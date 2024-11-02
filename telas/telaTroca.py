from abstratas.absTela import Tela


class TelaTroca(Tela):
    def tela_opcoes(self):
        print(f'-------TROCA-------')
        print(f'1 - Incluir Troca')
        print(f'2 - Excluir Troca')
        print(f'3 - Listar todas as Trocas')
        print(f'4 - Alterar Troca')
        print('0 - Retornar')        

        opcoes = int(input('Escolha uma opção para ver/cadastrar'))
        print()
        return opcoes

    def cadastrar_dados(self):
        nome = input('Digite o nome da pessoa: ')
        quantidade_usd = input('Digite o quanto você quer trocar em usd')
        moeda_entrada = input('Digite o nome da moeda que será fornecida pelo cliente:')
        moeda_saida = input('Digite o nome da moeda desejada:')
        juros 