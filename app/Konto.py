class Konto:
    def __init__(self, imie, nazwisko, pesel : str, promocja=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.promocja = promocja
        self.saldo = 0
        if (not self.pesel.isdigit()) or len(self.pesel) != 11:
            self.pesel = "Pesel nie jest poprawny!"
            self.rok = "Rok nie odpowiada promocji!"
            self.promocja = "Promocja nie poprawna!"
        else:
            self.dodaj_wiek()
            self.sprawdz_promocje()
            self.sprawdz_poprawnosc_wieku_do_promocji()

    def sprawdz_promocje(self):
        if self.promocja is None:
            pass
        elif self.promocja is not None and len(self.promocja) == 8 and self.promocja.startswith("PROM_"):
            pass
        else:
            self.promocja = "Promocja nie poprawna!"

    def dodaj_wiek(self):
        if self.pesel == "Pesel nie jest poprawny":
            self.rok = "Rok nie odpowiada promocji!"
            return
        else:
            number = self.pesel
            year = int(number[0:2])
            month = int(number[2:4])
            day = int(number[4:6])
            year += {
                0: 1900,
                1: 2000,
                2: 2100,
                3: 2200,
                4: 1800,
            }[month // 20]
            month = month % 20
            self.rok = year

    def sprawdz_poprawnosc_wieku_do_promocji(self):
        if self.promocja is not None and self.promocja.startswith("PROM_"):
            if self.rok <= 1960:
                self.rok = "Rok nie odpowiada promocji!"
            else:
                self.saldo = 50



k = Konto("abc", "def", "00283699111", "PROM_XYZ")
print(k.pesel, k.rok, k.promocja, k.saldo)

