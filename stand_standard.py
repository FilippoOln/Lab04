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

    def __lt__(self, other):
        return self.__prezzo_finale < other.prezzo_finale


    def __str__(self):
        return (f"{self.__codice}: {self.__metri_quadri} mq - padiglione {self.__padiglione} - "
                f"prezzo={self.__prezzo_finale}€ - disponibile={self.__disponibile} - "
                f"espositore associato=({self.__espositore_associato})")
