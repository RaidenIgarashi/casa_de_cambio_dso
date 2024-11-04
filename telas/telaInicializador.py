class TelaInicializador():
    def tela_opcoes(self):
        print("------CASA DE CAMBIO E EMPRÉSTIMOS------")
        print("OPÇÕES:")
        print("1 - Cliente")
        print("2 - Moeda")
        print("3 - Troca")
        print("4 - Empréstimo")
        print("0 - Encerrar :(")
        try:
            opcao = int(input("Escolha uma opção: "))
            if 0 <= opcao <= 4:
                print()
                return opcao
            else:
                print("\n## Digite um número de 0 a 4. ##\n")
                return None
        except:
            print("\n## Opção digitada incorretamente. Tente novamente. ##\n")
            return None
        
        