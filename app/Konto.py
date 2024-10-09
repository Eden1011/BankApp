class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        if len(f"{self.pesel}") != 11:
            self.pesel = "Pesel nie jest poprawny!"
        self.saldo = 0
