import requests
import time

from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, NIP):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.podatek_eskpresu = 5
        if len(str(NIP)) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            if self.zapytanieDoMF(NIP):
                self.nip = NIP
            else:
                raise ValueError("Firma nie zarejestrowana!")

    @classmethod
    def zapytanieDoMF(cls, NIP):
        odp = requests.get(f"https://wl-api.mf.gov.pl/api/search/nip/{NIP}?date={time.strftime('%Y-%m-%d')}")
        print(f"Odpowiedz API: {odp.json()}")
        return odp.status_code == 200

    def przelew_ekspres(self, wartosc):
        super().przelew_ekspres(wartosc)
        if not self.saldo < 0:
            self.saldo -= self.podatek_eskpresu
            self.historia_przelewow.append(-5)

    def zaciagnij_kredyt(self, wartosc):
        if self.saldo >= (2 * wartosc) and any(x == -1755 for x in self.historia_przelewow):
            self.saldo += wartosc
