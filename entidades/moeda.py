class Moeda:
    def __init__(self, nome:str, regioes:list, cifra:str, valor_usd:float):
        self.__nome = nome
        self.__regioes = regioes
        self.__cifra = cifra
        self.__valor_usd = valor_usd

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def regioes(self):
        return self.__regioes

    @regioes.setter
    def regioes(self, regioes):
        self.__regioes = regioes

    @property
    def cifra(self):
        return self.__cifra

    @cifra.setter
    def cifra(self, cifra):
        self.__cifra = cifra

    @property
    def valor_usd(self):
        return self.__valor_usd

    @valor_usd.setter
    def valor_usd(self, valor_usd):
        self.__valor_usd = valor_usd

    def add_regiao(self, regiao):
        if isinstance(regiao, str):
            for reg in self.regioes:
                if reg == regiao:
                    print('Essa região já está cadastrada')
                    return None
            self.__regioes.append(regiao)
        else:
            print('A região não foi entregue de forma correta')

    def show_regioes(self):
        regioes_str = ''
        for ind in range(self.__regioes):
            if ind < len(self.__regioes)-1:
                regioes_str += f'{self.__regioes[ind]}, '
            else:
                regioes_str += f'{self.__regioes[ind]}'
        return regioes_str

    def mostrar_infos(self):
        return f'Nome: {self.__nome}, Regiões: {self.show_regioes()}, Símbolo: {self.__cifra}, Valor em dólar: {self.__valor_usd}'
    
