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
        id = int(input('Digite o id da troca: '))
        nome = input('Digite o nome da pessoa: ')
        quantidade_pegada = input('Digite o quanto você quer trocar: ')
        moeda_entrada = input('Digite o nome da moeda que será fornecida pelo cliente:')
        moeda_saida = input('Digite o nome da moeda desejada: ')
        juros = float(input('Digite o juros que será aplicado: '))
        data = input('Digite a data da transação no estilo XX/XX/XXXX')

        return {'id': id, 'nome': nome, 'quantidade_usd': quantidade_pegada, 'moeda_entrada': moeda_entrada, 'moeda_saida': moeda_saida, 'juros': juros, 'data':data}

    def mostrar_dados(self, dados_troca):
        print('--------INFORMAÇÕES DA TROCA--------')
        print(f'NOME: {dados_troca["nome"]}')
        print(f'QUANTIDADE TROCADA: {dados_troca["quantidade_usd"]}')
        print(f'MOEDA ENTREGUE: {dados_troca["moeda_entrada"]}')
        print(f'MOEDA RECEBIDA: {dados_troca["moeda_saida"]}')
        print(f'JUROS: {dados_troca["juros"]}')
        print('\n')

    def mostrar_msg(self, msg):
        print(msg)

    def excluir(self):
        id = int(input('Escreva o id da troca que deseja excluir: '))
        return id 

    def alterar_dados(self):
        id = int(input('Escreva o id da troca que deseja alterar: '))
        return id 

    def ver_dados(self):
        id = int(input('Escreva o id da troca que deseja ver: '))
        return id


