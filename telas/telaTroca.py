from abstratas.absTela import Tela


class TelaTroca(Tela):
    def tela_opcoes(self):
        print(f'-------TROCA-------')
        print(f'1 - Ver dados de uma Troca')
        print(f'2 - Incluir Troca')
        print(f'3 - Excluir Troca')
        print(f'4 - Listar todas as Trocas')
        print(f'5 - Alterar Troca')
        print('0 - Retornar')        

        try:
            opcao = int(input("Escolha uma opção: "))
            if 0 <= opcao <= 5:
                print()
                return opcao
            else:
                print("\n## Digite um número de 0 a 5. ##\n")
                return None
        except:
            print("\n## Opção digitada incorretamente. Tente novamente. ##\n")
            return None

    def cadastrar_dados(self):
        try:
            id = int(input('Digite o id da troca: '))
        except(ValueError):
            print()
            print('## O ID precisa ser um número sem vígula ##')
            print()
            return
        try:
            id_pessoa = input('Digite o cpf da pessoa: ')
            id_pessoa_verify = id_pessoa.replace('.', '')
            if len(id_pessoa_verify) != 3:
                raise ValueError('## entrada não corresponde a um cpf ##')
        except ValueError as e:
            print()
            print(e)
            print()
            return
        moeda_entrada = input('Digite o nome da moeda que o cliente tem para trocar: ')
        moeda_saida = input('Digite o nome da moeda que o cliente quer receber: ')
        try:
            quantidade_entrada = float(input(f'Digite o quanto de "{moeda_entrada}" o cliente quer trocar por "{moeda_saida}": '))
        except:
            print()
            print(' ## Isso não e uma quantia ## ')
            print()
            return
        try:
            juros = float(input('Digite o juros que será aplicado (em %): ')) / 100
            if juros > 1:
                raise ValueError
        except:
            print()
            print('## O valor escrito não é um juros ##')
            print()
            return
        try:
            data = input('Digite a data da transação (dd/mm/aaaa): ')
            data_sem_barra = data.replace('/', '')
            if len(data_sem_barra) != 8:
                raise ValueError
            data_sem_barra = int(data_sem_barra)
        except:
            print()
            print('## esse valor não é uma data ##')
            print()
            return

        return {'id': id, 'id_pessoa': id_pessoa, 'quantidade_entrada': quantidade_entrada, 'quantidade_saida': 0, 'moeda_entrada': moeda_entrada, 'moeda_saida': moeda_saida, 'juros': juros, 'data':data}

    def mostrar_dados(self, dados_troca):
        print('--------INFORMAÇÕES DA TROCA--------')
        print(f'ID: {dados_troca["id"]}')
        print(f'CPF DO CLIENTE: {dados_troca["id_pessoa"]}')
        print(f'MOEDA ENTREGUE: {dados_troca["moeda_entrada"]}')
        print(f'MOEDA RECEBIDA: {dados_troca["moeda_saida"]}')
        print(f'QUANTIA DA MOEDA DE ENTRADA {dados_troca["moeda_entrada"]} = {dados_troca["quantidade_entrada"]:.2f}')
        print(f'QUANTIA DA MOEDA DE SAIDA {dados_troca["moeda_saida"]} = {dados_troca["quantidade_saida"]:.2f}')       
        print(f'JUROS: {dados_troca["juros"]*100}%')
        print('\n')

    def mostrar_msg(self, msg):
        print(msg)

    def excluir(self):
        try:
            id = int(input('Escreva o id da troca que deseja excluir: '))
            print()
            return id 
        except:
            print('\n## O ID deve ser apenas numérico ##\n')
            return
        

    def alterar_dados(self):
        try:
            id = int(input('Escreva o id da troca que deseja alterar: '))
            print()
            return id 
        except:
            print('## O ID deve ser apenas numérico ##')
            print()
            return

    def ver_dados(self):
        try:
            id = int(input('Escreva o id da troca que deseja ver: '))
            print()
            return id
        except:
            print('## o ID deve ser apenas numérico ##')
            print()
            return


