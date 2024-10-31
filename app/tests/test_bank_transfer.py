import unittest

from ..KontoPrywatne import KontoPrywatne as Konto

class TestPrzelewBankAccount(unittest.TestCase):

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