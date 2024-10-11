class Konto:
    def __init__(self, imie, nazwisko, pesel, promocja=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.promocja = promocja
        if len(f"{self.pesel}") != 11:
            self.pesel = "Pesel nie jest poprawny!"
        self.saldo = 0

        self.sprawdz_promocje()

    def sprawdz_promocje(self):
        if self.promocja is None:
            pass
        elif self.promocja is not None and len(self.promocja) == 8 and self.promocja.startswith("PROM_"):
            pass
        else:
            self.promocja = "Promocja nie poprawna!"

