import unittest

from ..KontoFirmowe import KontoFirmowe
from ..KontoPrywatne import KontoPrywatne as Konto

class TestPrzelewBankAccount(unittest.TestCase):

    def test_czy_da_sie_odebrac_zerowy_przelew(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        stare_saldo = pierwsze_konto.saldo
        pierwsze_konto.przelew_przychodzacy(0)
        self.assertEqual(stare_saldo + 0, pierwsze_konto.saldo, "Saldo konta nie jest poprawne")

    def test_czy_przelew_przychodzacy_dziala(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        stare_saldo = pierwsze_konto.saldo
        pierwsze_konto.przelew_przychodzacy(50)
        self.assertEqual(stare_saldo + 50, pierwsze_konto.saldo, "Saldo konta nie jest poprawne")

    def test_czy_przelew_wychodzacy_dziala(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.saldo = 100
        stare_saldo = pierwsze_konto.saldo

        pierwsze_konto.przelew_wychodzacy(50)
        self.assertEqual(stare_saldo - 50, pierwsze_konto.saldo, "Saldo konta nie jest poprawne")

    def test_czy_przelew_wychodzacy_niedziala(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.saldo = 10
        stare_saldo = pierwsze_konto.saldo
        pierwsze_konto.przelew_wychodzacy(50)
        self.assertEqual(pierwsze_konto.saldo, stare_saldo, "Saldo konta nie jest poprawne")

    def test_oplaty_zaksiegowania_dla_firm(self):
        nazwa="abd"
        nip=1234567890
        pierwsze_konto=KontoFirmowe(nazwa, nip)
        pierwsze_konto.saldo=51
        pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(pierwsze_konto.saldo, -4, "Saldo konta nie jest poprawne")

    def test_czy_mozna_wysylac_przelewy_z_ujemnym_saldem(self):
        nazwa = "abd"
        nip = 1234567890
        pierwsze_konto = KontoFirmowe(nazwa, nip)
        pierwsze_konto.saldo = -5
        pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(pierwsze_konto.saldo, -5, "Saldo konta nie jest poprawne")

    def test_czy_mozna_wysylac_przelewy_z_ujemnym_saldem_dla_kont_prywatnych(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.saldo = -1
        pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(pierwsze_konto.saldo, -1, "Saldo konta nie jest poprawne")
