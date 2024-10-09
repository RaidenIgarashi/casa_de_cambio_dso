from tela import Tela


class Tela_Organizacao(Tela):
    def tela_opcoes():
        print('-------ORGANIZAÇÕES-------')
        print('1 - Incluir organização')
        print('2 - Excluir organização')
        print('3 - Listar organização')
        print('4 - Alterar organização')
        print('0 - Retornar')

        opcao = int(input("Escolha uma Opção"))
        return opcao

    def pegar_dados(self):
        print('-------CADASTRE SUA ORGANIZAÇÃO--------')
        nome = str(input('Digite o nome de sua Organização'))
        cnpj = str(input('Digite seu cnpj'))
        return {nome:nome, cnpj:cnpj}
    
    def monstrar(self, dados_organizacao):
        print('--------INFORMAÇÕES--------')
        print(f'NOME DA ORGANIZAÇÃO: {dados_organizacao['nome']}')
        print(f'CNPJ DA ORGANIZAÇÃO: {dados_organizacao['cnpj']}')
        print("\n")

    def selecionar(self):
        cnpj = input('Digite o cnpj da organizacao que deseja achar')
        return cnpj

    def mostra_msg(self, msg):
        return super().mostra_msg(msg)


        