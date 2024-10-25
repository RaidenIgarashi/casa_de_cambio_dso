from abstratas.absTela import Tela


class TelaCliente(Tela):
    def tela_opcoes(self):
        print('-------CLIENTES-------')
        print('1 - Incluir cliente')
        print('2 - Excluir cliente')
        print('3 - Listar todos clientes')
        print('4 - Alterar cliente')
        print('0 - Retornar')

        opcao = int(input("Escolha uma Opção: "))
        return opcao

    def cadastrar_dados(self):
        print('-------CADASTRAR CLIENTE--------')
        tipo = input('Digite 0 para cadastrar Pessoa Física e 1 para cadastrar Organização: ')
        if tipo == "0": 
            nome = input('Digite o nome da pessoa: ')
            id = input('Digite o cpf da pessoa: ')
            idade = input('Digite a idade da pessoa: ')
            return {"nome":nome, "id":id, "idade":idade}
        else:
            nome = input('Digite o nome da organização: ')
            id = input('Digite o cnpj da organização: ')
            return {"nome":nome, "id":id}
        
    def alterar_dados(self):
        pass
        
    
    def mostrar(self, dados_organizacao):
        print('--------INFORMAÇÕES DOS CLIENTES--------')
        print(f'NOME: {dados_organizacao['nome']}')
        if 'idade' in dados_organizacao:
            print(f'CPF: {dados_organizacao['id']}')
            print(f'IDADE: {dados_organizacao['idade']}')
        else:
            print(f'CNPJ: {dados_organizacao['id']}')
        print(f'CRÉDITO: {dados_organizacao['credito_usd']}')
        print("\n")

    def selecionar(self):
        id = input('Digite o cpf/cnpj do cliente que deseja achar: ')
        return id

    def mostrar_msg(self, msg):
        print(msg)
