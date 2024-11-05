from abstratas.absTela import Tela
from datetime import date

class TelaEmprestimo(Tela):
    def tela_opcoes(self):
        print('-------EMPRESTIMO-------')
        print('1 - Registrar empréstimo')
        print('2 - Ver empréstimo registrado')
        print('3 - Excluir empréstimo')
        print('4 - Alterar empréstimo')
        print('5 - Registrar devolução de empréstimo')
        print('6 - Listar todos empréstimos')
        print('7 - Calcular valor de juros de um empréstimo')
        print('0 - Retornar')

        try:
            opcao = int(input("Escolha uma opção: "))
            if 0 <= opcao <= 7:
                print()
                return opcao
            else:
                print("\n## Digite um número de 0 a 7. ##\n")
                return None
        except:
            print("\n## Opção digitada incorretamente. Tente novamente. ##\n")
            return None

    def cadastrar_dados(self):
        print('-------REGISTRANDO EMPRÉSTIMO--------')
        try:
            id = int(input('Digite um id novo para a transação: '))
        except:
            print()
            print('## O ID deve ser um número ##')
            print()
            return
        cliente_id = input('Digite o cpf/cnpj do cliente que pediu o empréstimo: ')
        emprestador_id = input('Digite o cpf/cnpj do cliente que concedeu: ')
        moeda = input('Digite o nome da moeda utilizada: ')
        try:
            quantia = float(input('Digite a quantia repassada nesta moeda: '))
        except:
            print()
            print('## O valor digitado não é uma quantia ##')
            print()
        data_do_repasse = input('Digite a data em que foi feito o repasse [dd/mm/aaaa]: ')
        data_pretendida = input('Digite a data máxima combinada para devolução [dd/mm/aaaa]: ')
        try:
            juros_normal = int(input('Digite a quantidade de juros normal (em %) que será aplicado: '))
            juros_mensal_atraso = int(input('Digite a quantidade de juros (%) que será aplicado mensalmente em caso de atraso: '))
        except:
            print()
            print('## Valor digitado não corresponde a juros ##')
            print()
        dev = input('O empréstimo já foi devolvido e está sendo apenas registrado? 0- não, 1- sim: ')
        if dev == 1:
            devolvido = True
            data_devolvida = input('Digite a data em que o empréstimo foi devolvido [dd/mm/aaaa]: ')
        elif dev == 0:
            devolvido = False
            data_devolvida = None
            
        else:
            print("## opcao errada ##")
        return {'id':id, 'cliente_id':cliente_id, 'emprestador_id':emprestador_id, 'moeda':moeda, 'quantia':quantia, 
                'data_do_repasse':data_do_repasse, 'data_devolvida':data_devolvida, 'data_pretendida':data_pretendida, 
                'juros_normal':juros_normal, 'juros_mensal_atraso':juros_mensal_atraso, 'devolvido': devolvido}

    def mostrar_dados(self, dados_emprestimo):
        print('--------INFORMAÇÕES DO EMPRÉSTIMO--------')
        print(f'ID: {dados_emprestimo["id"]}')
        print(f'CLIENTE: {dados_emprestimo["cliente_id"]}')
        print(f'EMPRESTADOR: {dados_emprestimo["emprestador_id"]}')
        print(f'VALOR: {dados_emprestimo["quantia"]} {dados_emprestimo["moeda"]}(s)')
        print(f'DATAS: Repassado dia {dados_emprestimo["data_do_repasse"]}, com prazo até {dados_emprestimo["data_pretendida"]}.')
        print(f'JUROS: {dados_emprestimo["juros_normal"]}% + {dados_emprestimo["juros_mensal_atraso"]} por mês em caso de atraso.')
        if dados_emprestimo['devolvido']:
            print(f'SITUAÇÃO: DEVOLVIDO no dia {dados_emprestimo["data_devolvida"]}')
        else:
            print('SITUAÇÃO: NÃO devolvido')
        print('\n')

    def ver_juros(self):
        id = input('Escreva o id do empréstimo a qual deseja ver o valor do juros: ')
        return id
    def escolher_data(self):
        data = input('Escreva a data em qual se quer ver o possível valor acumulado: ')
        return data
        
    def emprestimo_devolvido(self):
        id = input('Escreva o id do empréstimo a qual se deseja registrar devolução: ')
        data = input('Escreva a data em que o dinheiro foi devolvido: ')
        return {'id':id, 'data':data}


    def excluir(self):
        id = input('Escreva o id do empréstimo que deseja excluir: ')
        return id 

    def alterar_dados(self):
        id = input('Escreva o id do empréstimo que deseja alterar: ')
        return id

    def ver_dados(self):
        id = input('Escreva o id do empréstimo que deseja ver: ')
        return id

    def mostrar_msg(self, msg):
        print(msg)
