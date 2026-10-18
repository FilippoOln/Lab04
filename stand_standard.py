class StandStandard:
    def __init__(self, codice, metri_quadri, padiglione, prezzo_base):
        self.__codice = codice
        self.__metri_quadri = metri_quadri
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base
        self.__espositore_associato = None
        self.__disponibile = True
        self.__prezzo_finale = None


    @property
    def codice(self):
        return self.__codice

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    @property
    def disponibile(self):
        return self.__disponibile

    @disponibile.setter
    def disponibile(self, disponibile):
        self.__disponibile = disponibile

    @property
    def espositore_associato(self):
        return self.__espositore_associato

    @espositore_associato.setter
    def espositore_associato(self, espositore):
        self.__espositore_associato = espositore

    @property
    def prezzo_finale(self):
        return self.__prezzo_finale

    @prezzo_finale.setter
    def prezzo_finale(self, prezzo_finale):
        self.__prezzo_finale = prezzo_finale

    def calcolati_prezzo_finale(self):
        self.__prezzo_finale = self.__prezzo_base

    def __repr__(self):
        return (f"{type(self).__name__}: codice={self.__codice} - mq={self.__metri_quadri} - "
                f"padiglione={self.__padiglione} - espositore associato= ({self.__espositore_associato})"
                f" - disponibile={self.__disponibile} - prezzo ={self.__prezzo_finale}€")