import unittest

from parameterized import parameterized

from ..RejestrKont import RejestrKont
from ..KontoPrywatne import KontoPrywatne as Konto

class TestRejestrKont(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pierwsze_konto = Konto("Dariusz", "Januszewski", "55072345789")

    def setUp(self):
        RejestrKont.dodaj_konto(self.pierwsze_konto)

    def test_dodaj_konto_i_poprawna_liczba_rejestru(self):
        self.assertEqual(RejestrKont.pobierz_liczbe_kont(), 1)

    def test_znajdz_konto(self):
        self.assertEqual(RejestrKont.znajdz_konto("55072345789"), self.pierwsze_konto)

    def test_nie_znajdz_konta(self):
        self.assertEqual(RejestrKont.znajdz_konto("1"), None)
