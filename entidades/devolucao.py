from datetime import date


class Devolucao:
    def __init__(self, data_do_repasse:date, data_pretendida:date, juros_normal:float, 
                 juros_mensal_atraso:float, devolvido:bool, data_devolvida:date, quantia_repassada:float):
        self.__data_do_repasse = data_do_repasse
        self.__data_pretendida = data_pretendida
        self.__juros_normal = juros_normal
        self.__juros_mensal_atraso = juros_mensal_atraso
        self.__devolvido = devolvido
        self.__data_devolvida = data_devolvida
        self.__quantia_repassada = quantia_repassada

    def calcula_juros(self, data_a_ver):
        juros = self.__quantia_repassada * self.__juros_normal
        juros_extra = 0
        if data_a_ver > self.__data_do_repasse:
            n = self.__data_pretendida - self.__data_do_repasse
            juros_extra = self.__quantia_repassada * (1 + self.__juros_mensal_atraso)**n
        return {'jn':juros, 'je':juros_extra}


    @property
    def data_do_repasse(self):
        return self.__data_do_repasse

    @data_do_repasse.setter
    def data_do_repasse(self, data_do_repasse):
        self.__data_do_repasse = data_do_repasse

    @property
    def data_pretendida(self):
        return self.__data_pretendida

    @data_pretendida.setter
    def data_pretendida(self, data_pretendida):
        self.__data_pretendida = data_pretendida

    @property
    def juros_normal(self):
        return self.__juros_normal

    @juros_normal.setter
    def juros_normal(self, juros_normal):
        self.__juros_normal = juros_normal

    @property
    def juros_mensal_atraso(self):
        return self.__juros_mensal_atraso

    @juros_mensal_atraso.setter
    def juros_mensal_atraso(self, juros_mensal_atraso):
        self.__juros_mensal_atraso = juros_mensal_atraso

    @property
    def devolvido(self):
        return self.__devolvido

    @devolvido.setter
    def devolvido(self, devolvido):
        self.__devolvido = devolvido

    @property
    def data_devolvida(self):
        return self.__data_devolvida

    @data_devolvida.setter
    def data_devolvida(self, data_devolvida):
        if data_devolvida == None:
            self.__devolvido = False 
        else:
            self.__devolvido = True 
        self.__data_devolvida = data_devolvida
