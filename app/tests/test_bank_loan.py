import unittest

from parameterized import parameterized
from ..KontoPrywatne import KontoPrywatne as Konto

class TestBankLoan(unittest.TestCase):

    def setUp(self):
        self.pierwsze_konto = Konto("Dariusz", "Januszewski","82151166666" )
    @parameterized.expand([
        #(name, input, expected)
        ("czyste_konto", [], "Nie pozwolono na kredyt!"),
        ("mniej_niz_3_przelewy", [100, 200], "Nie pozwolono na kredyt!"),
        ("dokladnie_3_przelewy", [100, 200, 300], 999),
        ("3_rozne_przelewy", [100, 200, -100], "Nie pozwolono na kredyt!"),
        ("wiecej_niz_3_rozne_przelewy", [100, 200, 300, -100], "Nie pozwolono na kredyt!"),
        ("5_przelewow_ale_mniejsze_niz_w_kredytu", [1, 1, 1, 1, -1], "Nie pozwolono na kredyt!"),
        ("dokladnie_5_przelewow_i_sukces", [999, 999, 999, 999, 999], 999),
    ])
    def test_sprawdz_kredyt(self, name, input, expected):
        self.pierwsze_konto.historia_przelewow = input
        self.pierwsze_konto.zaciagnij_kredyt(999)
        self.assertEqual(self.pierwsze_konto.kwota_kredytu, expected)