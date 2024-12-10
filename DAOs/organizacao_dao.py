from DAOs.dao import DAO
from entidades.organizacao import Organizacao

class OrganizacaoDAO(DAO):
    def __init__(self):
        super().__init__("organizacao.pkl")

    def add(self, organizacao: Organizacao):
        if((organizacao is not None) and isinstance(organizacao, Organizacao)):
            super().add(organizacao.nome, organizacao)

    def update(self, organizacao: Organizacao):
        if((organizacao is not None) and isinstance(organizacao, Organizacao)):
            super().update(organizacao.nome, organizacao)

    def get(self, key:str):
            return super().get(key)

    def remove(self, key:str):
            return super().remove(key)