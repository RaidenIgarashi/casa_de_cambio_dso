from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao


def eh_pessoa(info): # funcao para facilitar de ver se é pessoa ou organizacao (por id ou por objeto msm)
        if isinstance(info, str):
            for char in info:
                if not char.isnumeric: # deixa o cpf só com números, tira todo o resto
                    info = info.replace(char, '')
            if len(info) == 11: #cpf
                return True            # eh como se cpf tivesse 3 numeros e cnpj 5 pra ficar mais facil de testar
            elif len(info) == 5: #cnpj
                return False
            else: #quantidade errada
                print('\n## a quantidade de números não é a de uma identidade ##\n')
        elif isinstance(info, Pessoa):
            return True
        elif isinstance(info, Organizacao):
            return False
        else:
            print('\n## erro interno: id em formato inválido ##\n') 
