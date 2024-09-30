from pessoa import Pessoa
from organizacao import Organizacao
from troca import Troca
from bancomoedas import BancoMoedas

banco = BancoMoedas()
banco.add_moeda(nome='Real', regioes=['Brasil'], cifra='R$', valor_usd=5.00)
banco.add_moeda(nome='Dólar', regioes=['EUA'], cifra='U$D', valor_usd=1)
#yan = Pessoa(nome='yan', cpf='15365849752', idade=19, credito_usd=0)