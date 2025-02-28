from .Konto import Konto


class KontoPrywatne(Konto):
    def __init__(self, imie, nazwisko, pesel, promocja=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self._pesel = None
        self.promocja = promocja
        self.kwota_kredytu = 0
        self.podatek_ekspresu = 1
        self.pesel = pesel
        self.wstep_do_Mail = "Twoja historia przelewow dla konta Prywatnego to:"

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, new_pesel):
        if (not str(new_pesel).isdigit()) or len(str(new_pesel)) != 11:
            self._pesel = "Pesel nie jest poprawny!"
            self.rok = "Rok nie odpowiada promocji!"
            self.promocja = "Promocja nie poprawna!"
        else:
            self._pesel = new_pesel
            self.dodaj_wiek()
            self.sprawdz_promocje()
            self.sprawdz_poprawnosc_wieku_do_promocji()

    def sprawdz_promocje(self):
        if self.promocja is not None and (len(self.promocja) != 8 or not self.promocja.startswith("PROM_")):
            self.promocja = "Promocja nie poprawna!"

    def dodaj_wiek(self):
        if self.pesel != "Pesel nie jest poprawny":
            number = self.pesel
            year = int(number[0:2])
            month = int(number[2:4])
            day = int(number[4:6])
            year += {0: 1900, 1: 2000, 2: 2100, 3: 2200, 4: 1800, }[month // 20]
            month = month % 20
            self.rok = year

    def sprawdz_poprawnosc_wieku_do_promocji(self):
        if self.promocja is not None and self.promocja.startswith("PROM_"):
            if self.rok <= 1960:
                self.rok = "Rok nie odpowiada promocji!"
                self.promocja = "Promocja nie poprawna!"
            else:
                self.saldo = 50

    def sprawdz_czy_3_ostatnie_elementy_historii_sa_przychodzacymi_przelewami(self, wartosc):
        if len(self.historia_przelewow) >= 3 and all(x > 0 for x in self.historia_przelewow[-3:]):
            self.kwota_kredytu = wartosc
        else:
            self.sprawdz_czy_ostatnie_5_maja_sume_wieksza_od_wartosci(wartosc)

    def sprawdz_czy_ostatnie_5_maja_sume_wieksza_od_wartosci(self, wartosc):
        if len(self.historia_przelewow) >= 5 and sum(self.historia_przelewow[-5:]) >= wartosc:
            self.kwota_kredytu = wartosc
        else:
            self.kwota_kredytu = "Nie pozwolono na kredyt!"

    def zaciagnij_kredyt(self, wartosc):
        self.sprawdz_czy_3_ostatnie_elementy_historii_sa_przychodzacymi_przelewami(wartosc)
        if self.kwota_kredytu != "Nie pozwolono na kredyt!":
            self.saldo += wartosc

    def przelew_ekspres(self, wartosc):
        super().przelew_ekspres(wartosc)
        if not self.saldo < 0:
            self.saldo -= self.podatek_ekspresu
            self.historia_przelewow.append(-1)
