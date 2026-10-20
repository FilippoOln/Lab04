class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice(self):
        return self.__codice

    def __eq__(self, otherObject):
        if isinstance(otherObject, Espositore):
            return self.__codice == otherObject.codice
        else :
            return False

    def __str__(self):
        return f"{self.__codice}: '{self.__nome} {self.__cognome}'"

