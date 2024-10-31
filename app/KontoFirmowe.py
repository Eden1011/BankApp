from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.nip = NIP
        if len(str(self.nip)) != 10:
            self.nip="Niepoprawny NIP!"

    def przelew_ekspres(self, wartosc):
        super().przelew_ekspres(wartosc)
        if not self.saldo < 0:
            self.saldo-=5