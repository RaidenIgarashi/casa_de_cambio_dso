from abstratas.absTela import Tela


class TelaPessoa(Tela):
    def tela_opcoes(self):
        print("------PESSOA-------")
        print("1 - Incluir pessoa")
        print("2 - Excluir pessoa")
        print("3 - Listar pessoa")
        print("4 - Alterar pessoa")
        print("0 - Retornar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pegar_dados(self):
        print("-------CADASTRE SUA PESSOA--------")
        nome = str(input("Digite o nome de pessoa: "))
        idade = int(input("Digite a idade da pessoa: "))
        id = str(input("Digite o cpf da pessoa: "))
        return {"nome":nome, "idade":idade, "id":id}

    def mostrar(self, dados_pessoa):
        print("--------INFORMAÇÕES--------")
        print(f"NOME DA PESSOA: {dados_pessoa["nome"]}")
        print(f"IDADE DA PESSOA: {dados_pessoa["idade"]}")
        print(f"CPF DA PESSOA: {dados_pessoa["id"]}")
        print(f"CREDITO_USD DA PESSOA: {dados_pessoa["credito_usd"]}")

        print("\n")

    def selecionar(self):
        id = input("Digite o cpf da pessoa que deseja achar: ")
        return id

    def mostra_msg(self, msg):
        return super().mostra_msg(msg)
