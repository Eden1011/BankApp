from .Konto import Konto

class KontoPrywatne(Konto):
    def __init__(self, imie, nazwisko, pesel, promocja=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.promocja = promocja
        self.kwota_kredytu=0


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
        if self.pesel != "Pesel nie jest poprawny":
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

    def zaciagnij_kredyt(self, wartosc):
        if len(self.historia_przelewow) >= 3:
            ostatnie_3_wplaty=self.historia_przelewow[-3:]
            mozna_kredyt = True
            for i in ostatnie_3_wplaty:
                if i < 0:
                    mozna_kredyt = False
                    break
            if mozna_kredyt:
                self.kwota_kredytu += wartosc
            else:
                if len(self.historia_przelewow) < 5:
                    mozna_kredyt = False
                    self.kwota_kredytu = "Nie pozwolono na kredyt!"
                else:
                    ostatnie_5_wplat_sum = sum(self.historia_przelewow[-5:])
                    if ostatnie_5_wplat_sum > wartosc:
                        mozna_kredyt = True
                        self.kwota_kredytu += wartosc
                    else:
                        self.kwota_kredytu = "Nie pozwolono na kredyt!"
        else:
            self.kwota_kredytu="Nie pozwolono na kredyt!"


    def przelew_ekspres(self, wartosc):
        super().przelew_ekspres(wartosc)
        if not self.saldo < 0:
            self.saldo -= 1
            self.historia_przelewow.append(-1)