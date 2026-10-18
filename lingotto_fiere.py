from csv import reader
from espositore import Espositore
from standPremium import StandPremium
from standConPrese import StandConPrese
from standStandard import StandStandard
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__lista_espositori = []
        self.__lista_stand = []

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            infile = open(file_path, "r")
            csvReader = reader(infile)

            for row in csvReader:
                num_campi = len(row)

                if num_campi == 3:
                    cod_espositore = row[0]
                    nome_espositore = row[1]
                    cogn_espositore = row[2]
                    espositore = Espositore(cod_espositore, nome_espositore, cogn_espositore)
                    self.__lista_espositori.append(espositore)

                else:
                    cod_stand = row[0]
                    metri_q = int(row[1])
                    padiglione = int(row[2])
                    prezzo_base = float (row[3])

                    if num_campi == 5:
                        if row[4].isdigit():
                            num_prese_extra = int(row[4])
                            stand = StandConPrese(cod_stand, metri_q, padiglione, prezzo_base, num_prese_extra)
                        else:
                            posizione = row[4]
                            stand = StandPremium(cod_stand, metri_q, padiglione, prezzo_base, posizione)

                    else:
                        stand = StandStandard(cod_stand, metri_q, padiglione, prezzo_base)

                    stand.calcolati_prezzo_finale()
                    self.__lista_stand.append(stand)

            infile.close()
            print("\nLista degli stand:")
            for stand in self.__lista_stand:
                print(repr(stand))

            print("---------------")

            print("Lista degliespositori:")
            for espositore in self.__lista_espositori:
                print(repr(espositore))

        except FileNotFoundError:
            raise FileNotFoundError(f"il file {file_path} non è stato trovato!!!!")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_cercato = None
        espositore_cercato = None

        for espositore in self.__lista_espositori:
            if espositore.codice == codice_espositore:
                espositore_cercato = espositore
                break

        if espositore_cercato is None:
            raise Exception(f"Non esiste nessun espositore con codice {codice_espositore}")

        for stand in self.__lista_stand:
            if stand.espositore_associato is not None:
                if stand.espositore_associato.codice == codice_espositore:
                    raise Exception(f"L'espositore {codice_espositore} è già associato allo stand {stand.codice}")

        for stand in self.__lista_stand:
            if stand.codice == codice_stand:
                stand_cercato = stand
                if  not stand_cercato.disponibile:
                    raise Exception(f"Lo stand {codice_stand} è gia assegnato all'espositore {stand_cercato.espositore_associato.codice}!!")
                else:
                    stand_cercato.disponibile = False
                    stand_cercato.espositore_associato = espositore_cercato

                break

        if stand_cercato is None:
            raise Exception(f"Non esiste nessuno stand con codice {codice_stand}")

        print("\nLista degli stand:")
        for stand in self.__lista_stand:
            print(repr(stand))

        print("---------------")

        print("Lista degli espositori:")
        for espositore in self.__lista_espositori:
            print(repr(espositore))


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        for espositore in self.__lista_espositori:
            stand_assegnato = None
            for stand in self.__lista_stand:
                if espositore == stand.espositore_associato:
                    stand_assegnato = stand
                    break

            if stand_assegnato is  not None:
                print(f"{espositore} che è assegnato allo stand {stand_assegnato}")
            else:
                print(f"{espositore}")




    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.__lista_stand, key=attrgetter("prezzo_finale"))




