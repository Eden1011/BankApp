import unittest
from operator import truediv
from unittest.mock import patch, mock_open

from parameterized import parameterized
from app.KontoPrywatne import KontoPrywatne as Konto
from app.KontoFirmowe import KontoFirmowe as KontoFirmowe


class TestBankLoan(unittest.TestCase):

    def setUp(self):
        self.pierwsze_konto = Konto("Dariusz", "Januszewski", "82151166666")

    @parameterized.expand([  # (name, input, expected)
        ("czyste_konto", [], "Nie pozwolono na kredyt!"),
        ("mniej_niz_3_przelewy", [100, 200], "Nie pozwolono na kredyt!"),
        ("dokladnie_3_przelewy", [100, 200, 300], 999),
        ("3_rozne_przelewy", [100, 200, -100], "Nie pozwolono na kredyt!"),
        ("wiecej_niz_3_rozne_przelewy", [100, 200, 300, -100], "Nie pozwolono na kredyt!"),
        ("5_przelewow_ale_mniejsze_niz_w_kredytu", [1, 1, 1, 1, -1], "Nie pozwolono na kredyt!"),
        ("5_przelewow_z_suma_wieksza_niz_kredyt", [1000, 1000, 1000, -100, 100], 999), ])
    def test_sprawdz_kredyt(self, name, input, expected):
        self.pierwsze_konto.historia_przelewow = input
        self.pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(self.pierwsze_konto.kwota_kredytu, expected)


class TestFirmBankLoan(unittest.TestCase):



    @parameterized.expand([("brakuje salda, oraz brakuje historii", (0, []), 0),
                           ("brakuje salda, ale nie brakuje historii", (0, [-1755]), 0),
                           ("nie brakuje salda, ani historii", (4, [-1755]), 6), ])
    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=True)
    def test_firma_kredyt(self, name, tuple, koncowe_saldo_expected, mock_zapytanieDoMF):
        self.pierwsze_konto = KontoFirmowe("abc", "8461627563")
        saldo_start = tuple[0]
        historia_przelewow_start = tuple[1]
        self.pierwsze_konto.saldo = saldo_start
        self.pierwsze_konto.historia_przelewow = historia_przelewow_start
        self.pierwsze_konto.zaciagnij_kredyt(2)
        self.assertEqual(self.pierwsze_konto.saldo, koncowe_saldo_expected)
