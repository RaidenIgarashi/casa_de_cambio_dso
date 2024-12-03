from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao
from excecoes import ComCaractere, NomeComDigito, ValorNaoNumerico


def eh_pessoa(info): # funcao para facilitar de ver se é pessoa ou organizacao (por id ou por objeto msm)
        if isinstance(info, str):
            for c in info:
                if not c.isalpha:
                    info.replace(c, '')

            if len(info) == 3: # CPF AQUI TEM 3 DIGITOS E CNPJ 5 PRA FACILITAR
                return True
            elif len(info) == 5:
                return False
            else: 
                print('\n## a quantidade de números não é a de uma identidade ##\n')
                return None
        elif isinstance(info, Pessoa):
            return True
        elif isinstance(info, Organizacao):
            return False
        else:
            print('\n## erro interno: id em formato inválido ##\n') 

def eh_numerico(x):
    numerico = True
    try:
        for c in x:
            if not c.isnumeric():
                numerico = False
        if not numerico:
            raise ComCaractere('números')
        return numerico
    except:
        raise ComCaractere('números')

def eh_alpha(x):
    alpha = True
    try:
        for c in x:
            if not c.isalpha():
                alpha = False
        if not alpha:
            raise NomeComDigito()
        return alpha
    except:
        raise NomeComDigito()

