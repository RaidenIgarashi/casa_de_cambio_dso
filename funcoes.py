from entidades.pessoa import Pessoa
from entidades.organizacao import Organizacao
from excecoes import *


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
                return None
        elif isinstance(info, Pessoa):
            return True
        elif isinstance(info, Organizacao):
            return False

def eh_numerico(valor, variavel):
    numerico = True
    try:
        if valor == '' or valor == None:
            numerico = False
        else:
            for c in valor:
                if not c.isnumeric():
                    numerico = False
            if not numerico:
                NaoNumericoGeral(variavel)
        return numerico
    except:
        NaoNumericoGeral(variavel)

def eh_alpha(x):
    alpha = True
    try:
        for c in x:
            if not c.isalpha():
                alpha = False
        if not alpha:
            NomeComDigito()
        return alpha
    except:
        NomeComDigito()

