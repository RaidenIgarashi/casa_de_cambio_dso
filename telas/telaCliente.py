from abstratas.absTela import Tela


class TelaCliente(Tela):
    def tela_opcoes(self):
        print('-------CLIENTES-------')
        print('1 - Incluir cliente')
        print('2 - Excluir cliente')
        print('3 - Listar cliente')
        print('4 - Alterar cliente')
        print('0 - Retornar')

        opcao = int(input("Escolha uma Opção: "))
        return opcao

    def pegar_dados(self):
        print('-------CADASTRAR CLIENTE--------')
        nome = str(input('Digite o nome do cliente: '))
        id = str(input('Digite seu cpf/cnpj: '))
        return {"nome":nome, "id":id}
    
    def mostrar(self, dados_organizacao):
        print('--------INFORMAÇÕES DOS CLIENTES--------')
        print(f'NOME: {dados_organizacao['nome']}')
        print(f'CPF/CNPJ: {dados_organizacao['id']}')
        print(f'CRÉDITO: {dados_organizacao['credito_usd']}')
        print("\n")

    def selecionar(self):
        id = input('Digite o cnpj da organizacao que deseja achar: ')
        return id

    def mostra_msg(self, msg):
        return super().mostra_msg(msg)


        