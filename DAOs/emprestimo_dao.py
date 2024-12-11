from DAOs.dao import DAO
from entidades.emprestimo import Emprestimo

class EmprestimoDAO(DAO):
    def __init__(self):
        super().__init__('DAOs/pickles/emprestimo.pkl')

    def add(self, emprestimo: Emprestimo):
        if((emprestimo is not None) and isinstance(emprestimo, Emprestimo)):
            super().add(emprestimo.id, emprestimo)

    def update(self, emprestimo: Emprestimo):
        if((emprestimo is not None) and isinstance(emprestimo, Emprestimo)):
            super().update(emprestimo.id, emprestimo)

    def get(self, key:str):
            return super().get(key)

    def remove(self, key:str):
            return super().remove(key)
    