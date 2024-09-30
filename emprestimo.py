from pessoa import Pessoa
from organizacao import Organizacao
from moeda import Moeda


class Emprestimo:
    def __init__(self, id:int, cliente, emprestador, quantidade_usd:float, data:str, 
                 moeda_pedida:Moeda, moeda_entregue:Moeda, juros_mensal:int):
        self.__id = id
        if not (cliente == Organizacao and emprestador == Pessoa):
            self.__cliente = cliente
            self.__emprestador = emprestador
        self.__quantidade_usd = quantidade_usd
        self.__data = data
        self.__moeda_pedida = moeda_pedida
        self.__moeda_entregue = moeda_entregue
        self.__juros_mensal = juros_mensal
        self.__emprestimo_pago = False




    def ver_estado_emprestimo(self, data):
        qnt = self.__quantidade_usd
        juros = self.__juros_mensal
        nome = self.__cliente
        t = data - self.__data    #fazer com que 't' seja a quantidade de meses da data de empréstimo pra data pedida
        mped = self.__moeda_pedida
        ment = self.__moeda_entregue
        print(f'Empréstimo com valor de ${qnt} dólares feita por {nome}, no dia {data}. O cliente pegou emprestado \
              {mped.__cifra}{mped*mped.__valor_usd} e deve devolver {ment.__cifra}{ment*ment.__valor_usd} com {juros/100} de juros mensal. \
              nesta data, a quantidade a se pagar com juros cumulativo é de {qnt * (1 + (juros/100))**t}')
