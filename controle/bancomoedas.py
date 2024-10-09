from entity.moeda import Moeda


class BancoMoedas:
    def __init__(self):
        self.__moedas = []

    def add_moeda(self, nome:str, regioes:list, cifra:str, valor_usd:float):
        m = Moeda(nome, regioes, cifra, valor_usd)
        self.__moedas.append(m)

    def del_moeda(self, nome_moeda):
        for m in self.__moedas:
            if m.nome == nome_moeda:
                self.__moedas.remove(m)
                break

    def ver_todas_moedas(self):
        for m in self.__moedas:
            print(m.mostrar_infos())

    def pegar_moeda(self, nome_moeda):
        for m in self.__moedas:
            if m.nome == nome_moeda:
                return m
