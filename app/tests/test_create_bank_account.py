import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 32154365499
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel, "Pesel nie jest poprawny!")

    def test_np_pesel(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 321
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Pesel nie jest poprawny!", "Pesel nie jest poprawny!")

    def test_p_promocja(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 32154365499
        promocja="PROM_123"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        self.assertEqual(pierwsze_konto.promocja, promocja, "Promocja nie poprawna!")

    def test_np_promocja(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = 32154365499
        promocja="PROM_"
        pierwsze_konto = Konto(imie, nazwisko, pesel, promocja)
        self.assertEqual(pierwsze_konto.promocja,"Promocja nie poprawna!" , "Promocja nie poprawna!")

    #tutaj proszę dodawać nowe testy