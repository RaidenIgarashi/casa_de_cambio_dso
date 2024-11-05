from abstratas.absTela import Tela
from controladores.funcoes import eh_pessoa

class TelaCliente(Tela):
    def tela_opcoes(self):
        print(f'-------ClIENTES-------')
        print(f'1 - Ver dados de um cliente')
        print(f'2 - Adicionar cliente')
        print(f'3 - Excluir cliente')
        print(f'4 - Alterar cliente')
        print(f'5 - Listar tudo de clientes')
        print(f'6 - Mostrar transações de um cliente')
        print(f'0 - Retornar')

        try:
            opcao = int(input("Escolha uma opção: "))
            if 0 <= opcao <= 6:
                print()
                return opcao
            else:
                print("\n## Digite um número de 0 a 6. ##\n")
                return None
        except:
            print("\n## Opção digitada incorretamente. Tente novamente. ##\n")
            return None

    def cadastrar_dados(self):
        print('-------CADASTRAR CLIENTE--------')
        try:
            tipo = int(input('Digite 0 para cadastrar Pessoa Física e 1 para cadastrar Organização: '))
            if tipo < 0 or tipo > 1:
                raise ValueError
        except:
            print()
            print('## As únicas entradas possíveis são 0 e 1 ##')
            print()
            return

        if tipo == 0: 
            try:
                nome = input('Digite o nome da pessoa: ')
                for char in nome:
                    if char.isnumeric():
                        raise ValueError
            except:
                print()
                print('## Não coloque números no nome ##')
                print()
                return
            id = input('Digite o cpf da pessoa: ')
            try:
                idade = int(input('Digite a idade da pessoa: '))
            except:
                print()
                print('## idade deve ser apenas numérica')
                print()
                return
            print()
        
            return {"nome":nome, "id":id, "idade":idade}
        elif tipo == 1:
            try:
                nome = input('Digite o nome da organização: ')
                for char in nome:
                    if char.isnumeric():
                        raise ValueError
            except:
                print()
                print('## Não coloque números no nome ##')
                print()
                return
            id = input('Digite o cnpj da organização: ').strip()
            print()
            return {"nome":nome, "id":id}
        
        
    def alterar_dados(self):
        id = input('Digite o cpf/cnpj do cliente que deseja alterar: ')
        print()
        return id
    
    def mostrar_dados(self, dados_cliente):
        print('--------INFORMAÇÕES DO CLIENTE--------')
        print(f"NOME: {dados_cliente['nome']}")
        if 'idade' in dados_cliente:
            print(f"CPF: {dados_cliente['id']}")
            print(f"IDADE: {dados_cliente['idade']}")
        else:
            print(f"CNPJ: {dados_cliente['id']}")
        print()

    def excluir(self):
        id = input('Digite o cpf/cnpj do cliente que deseja excluir: ')
        print()
        return id
    
    def ver_transacoes(self):
        id = input('Digite o cpf/cnpj do cliente que deseja ver todas as transações feitas: ')
        print()
        return id

    def ver_dados(self):
        id = input('Digite o cpf/cnpj do cliente que deseja ver os dados: ')
        print()
        return id
    
    def mostrar_msg(self, msg):
        super().mostrar_msg(msg)
    