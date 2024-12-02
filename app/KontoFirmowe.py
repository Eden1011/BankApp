from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.nip = NIP
        self.podatek_eskpresu = 5
        if len(str(self.nip)) != 10:
            self.nip = "Niepoprawny NIP!"

    def przelew_ekspres(self, wartosc):
        super().przelew_ekspres(wartosc)
        if not self.saldo < 0:
            self.saldo -= self.podatek_eskpresu
            self.historia_przelewow.append(-5)

    def zaciagnij_kredyt(self, wartosc):
        if self.saldo >= (2 * wartosc) and any(x == -1755 for x in self.historia_przelewow):
            self.saldo += wartosc
