from standStandard import StandStandard

class StandConPrese(StandStandard):
    def __init__(self,codice, metri_quadri, padiglione, prezzo_base, num_prese_extra):
        super().__init__(codice, metri_quadri, padiglione, prezzo_base)
        self.__num_prese_extra = num_prese_extra


    def calcolati_prezzo_finale(self):
        self.prezzo_finale = round(((1 + 0.07 * self.__num_prese_extra) * super().prezzo_base), 2)


    def __repr__(self):
        return f"{super().__repr__()} - num prese extra={self.__num_prese_extra}"
