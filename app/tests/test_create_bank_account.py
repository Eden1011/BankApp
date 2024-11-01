import unittest

from ..KontoPrywatne import KontoPrywatne as Konto
from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "32154365499"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "Pesel nie jest poprawny!")

    def test_np_pesel(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "321"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Pesel nie jest poprawny!", "Pesel nie jest poprawny!")
    def test_np_wiek_z_pesela(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "321"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Pesel nie jest poprawny!", "Pesel nie jest poprawny!")
        self.assertEqual(pierwsze_konto.rok, "Rok nie odpowiada promocji!", "Rok nie odpowiada promocji!")

    def test_p_promocja(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "32154365499"
        promocja="PROM_123"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        self.assertEqual(pierwsze_konto.promocja, promocja, "Promocja nie poprawna!")

    def test_np_promocja(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "32154365499"
        promocja="PROM_"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        self.assertEqual(pierwsze_konto.promocja,"Promocja nie poprawna!" , "Promocja nie poprawna!")

    def test_p_wiek(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        promocja="PROM_123"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        rok_seniorka = pierwsze_konto.rok
        self.assertGreater(rok_seniorka, 1960, "Rok nie odpowiada promocji!" )

    def test_np_wiek(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "32154365499"
        promocja = "PROM_123"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        self.assertEqual(pierwsze_konto.rok, "Rok nie odpowiada promocji!", "Rok nie odpowiada promocji!")

    def test_dodano_rabat_do_salda_po_udanej_promocji(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        promocja = "PROM_123"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        rok_seniorka = pierwsze_konto.rok
        self.assertEqual(pierwsze_konto.saldo, 50, "Nie dodano rabatu!")

    def test_czy_saldo_jest_puste_po_nie_udanej_promocji(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        promocja = "PROM_"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        rok_seniorka = pierwsze_konto.rok
        self.assertEqual(pierwsze_konto.saldo, 0, "Nie dodano rabatu!")

    def test_nip_konta_firmowego_nie_poprawne(self):
        nazwa_firmy="adsv"
        NIP=123456789
        pierwsze_konto=KontoFirmowe(nazwa_firmy, NIP)
        self.assertEqual(pierwsze_konto.nip, "Niepoprawny NIP!", "Niepoprawny NIP!")

    def test_nip_konta_firmowego_poprawne(self):
        nazwa_firmy="adsv"
        NIP=1234567890
        pierwsze_konto=KontoFirmowe(nazwa_firmy, NIP)
        self.assertEqual(pierwsze_konto.nip, NIP, "Niepoprawny NIP!")