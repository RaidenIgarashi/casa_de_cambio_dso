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
        print('0 - Retornar')

        opcoes = int(input("Escolha uma opção para ver/cadastrar: "))
        print()
        return opcoes

    def cadastrar_dados(self):
        print('-------CADASTRAR CLIENTE--------')
        tipo = input('Digite 0 para cadastrar Pessoa Física e 1 para cadastrar Organização: ')
        if tipo == "0": 
            nome = input('Digite o nome da pessoa: ')
            id = input('Digite o cpf da pessoa: ')
            idade = input('Digite a idade da pessoa: ')
            print()
            return {"nome":nome, "id":id, "idade":idade}
        else:
            nome = input('Digite o nome da organização: ')
            id = input('Digite o cnpj da organização: ')
            print()
            return {"nome":nome, "id":id}
        
        
    def alterar_dados(self):
        id = input('Digite o cpf/cnpj do cliente que deseja alterar: ')
        print()
        return id
    
    def mostrar_dados(self, dados_cliente):
        print('--------INFORMAÇÃO DO CLIENTE--------')
        print(f'NOME: {dados_cliente['nome']}')
        if eh_pessoa(dados_cliente['id']):
            print(f'CPF: {dados_cliente['id']}')
            print(f'IDADE: {dados_cliente['idade']}')
        else:
            print(f'CNPJ: {dados_cliente['id']}')
        print(f'CRÉDITO: U$D{dados_cliente['credito_usd']:.2f}')
        print()

    def excluir(self):
        id = input('Digite o cpf/cnpj do cliente que deseja fazer esta alteração: ')
        print()
        return id

    def ver_dados(self):
        id = input('Digite o cpf/cnpj do cliente que deseja ver os dados: ')
        print()
        return id
    
    def mostrar_msg(self, msg):
        super().mostrar_msg(msg)
    
