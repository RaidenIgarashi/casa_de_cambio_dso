from abstratas.absTela import Tela


class TelaTroca(Tela):
    def tela_opcoes(self):
        print(f'-------TROCA-------')
        print(f'1 - Incluir Troca')
        print(f'2 - Excluir Troca')
        print(f'3 - Listar todas as Trocas')
        print(f'4 - Alterar Troca')
        print('0 - Retornar')        

        opcoes = int(input('Escolha uma opção para ver/cadastrar: '))
        print()
        return opcoes

    def cadastrar_dados(self):
        id = int(input('Digite o id da troca: '))
        id_pessoa = input('Digite o cpf da pessoa: ')
        quantidade_entrada = float(input('Digite o quanto você quer trocar: '))
        moeda_entrada = input('Digite o nome da moeda que será fornecida pelo cliente: ')
        moeda_saida = input('Digite o nome da moeda desejada: ')
        juros = float(input('Digite o juros que será aplicado: '))
        data = input('Digite a data da transação no estilo XX/XX/XXXX: ')

        return {'id': id, 'id_pessoa': id_pessoa, 'quantidade_entrada': quantidade_entrada, 'quantidade_saida': 0, 'moeda_entrada': moeda_entrada, 'moeda_saida': moeda_saida, 'juros': juros, 'data':data}

    def mostrar_dados(self, dados_troca):
        print('--------INFORMAÇÕES DA TROCA--------')
        print(f'ID: {dados_troca["id"]}')
        print(f'CPF DO CLIENTE: {dados_troca["id_pessoa"]}')
        print(f'MOEDA ENTREGUE: {dados_troca["moeda_entrada"]}')
        print(f'MOEDA RECEBIDA: {dados_troca["moeda_saida"]}')
        print(f'QUANTIA DA MOEDA DE ENTRADA {dados_troca["moeda_entrada"]}: {dados_troca["quantidade_entrada"]}')
        print(f'QUANTIA DA MOEDA DE SAIDA {dados_troca["moeda_saida"]}: {dados_troca["quantidade_saida"]}')       
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


