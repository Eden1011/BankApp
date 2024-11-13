import unittest
from ..KontoPrywatne import KontoPrywatne as Konto

class TestBankLoan(unittest.TestCase):
    def test_czy_mozna_wziasc_kredyt_jesli_konto_ma_mniej_niz_3_przelewy(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(pierwsze_konto.kwota_kredytu, "Nie pozwolono na kredyt!", "Nie pozwolono na kredyt!")

    def test_czy_mozna_wziasc_kredyt_jesli_konto_sie_3_przelewy_przychodzace(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.przelew_przychodzacy(300)
        pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(pierwsze_konto.kwota_kredytu, 999, "Nie pozwolono na kredyt!")
    def test_czy_mozna_wziasc_kredyt_jesli_konto_nie_ma_3_przelewow_przychodzacych(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.przelew_wychodzacy(300)
        pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(pierwsze_konto.kwota_kredytu, "Nie pozwolono na kredyt!", "Nie pozwolono na kredyt!")

    def test_czy_mozna_wziasc_kredyt_jak_ma_sie_4_rozne_przelewy_w_historii(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.przelew_przychodzacy(300)
        pierwsze_konto.przelew_wychodzacy(100)
        pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(pierwsze_konto.kwota_kredytu, "Nie pozwolono na kredyt!", "Nie pozwolono na kredyt!")

    def test_czy_mozna_wziasc_kredyt_jak_ma_sie_5_lub_wiecej_roznych_przelewow_ale_mniejsze_niz_wartosc_kredytu(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_wychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.zaciagnij_kredyt(1337)
        self.assertEqual(pierwsze_konto.kwota_kredytu, "Nie pozwolono na kredyt!", "Nie pozwolono na kredyt!")

    def test_czy_mozna_wziasc_kredyt_jak_ma_sie_5_lub_wiecej_roznych_przelewow_wieksych_niz_wartosc_kredytu(self):
        imie = "Dariusz"
        nazwisko = "Januszewski"
        pesel = "82151166666"
        pierwsze_konto = Konto(imie, nazwisko, pesel)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(100)
        pierwsze_konto.przelew_wychodzacy(100)
        pierwsze_konto.przelew_przychodzacy(200)
        pierwsze_konto.zaciagnij_kredyt(50)
        self.assertEqual(pierwsze_konto.kwota_kredytu, 50, "Nie pozwolono na kredyt!")

