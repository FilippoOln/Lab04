from standStandard import StandStandard

class StandPremium(StandStandard):
    def __init__(self, codice, metri_quadri, padiglione, prezzo_base, posizione):
        super().__init__(codice, metri_quadri, padiglione, prezzo_base)
        self.__posizione = posizione


    def calcolati_prezzo_finale(self):
        self.prezzo_finale = round((1.30 * super().prezzo_base), 2)


    def __repr__(self):
        return f"{super().__repr__()} - posizione={self.__posizione}"