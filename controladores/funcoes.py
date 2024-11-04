from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao


def eh_pessoa(info): # funcao para facilitar de ver se é pessoa ou organizacao (por id ou por objeto msm)
        if isinstance(info, str):
            info = info.replace('.', '')

            if len(info) == 11:
                 return True
            info = info.replace('/', '')
            if len(info) == 14:
                 return False
            else: #quantidade errada
                print('\n## a quantidade de números não é a de uma identidade ##\n')
                return None
        elif isinstance(info, Pessoa):
            return True
        elif isinstance(info, Organizacao):
            return False
        else:
            print('\n## erro interno: id em formato inválido ##\n') 
