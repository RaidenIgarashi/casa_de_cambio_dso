from DAOs.dao import DAO
from entidades.troca import Troca

class TrocaDAO(DAO):
    def __init__(self):
        super().__init__('troca.pkl')

    def add(self, troca: Troca):
        if((troca is not None) and isinstance(troca, Troca)):
            super().add(troca.id, troca)

    def update(self, troca: Troca):
        if((troca is not None) and isinstance(troca, Troca)):
            super().update(troca.id, troca)

    def get(self, key:str):
            return super().get(key)

    def remove(self, key:str):
            return super().remove(key)