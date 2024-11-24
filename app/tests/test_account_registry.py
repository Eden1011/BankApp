import unittest

from parameterized import parameterized

from ..RejestrKont import RejestrKont
from ..KontoPrywatne import KontoPrywatne as Konto

class TestRejestrKont(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pierwsze_konto = Konto("Dariusz", "Januszewski", "55072345789")
        cls.drugie_konto = Konto("Ania", "Janosik","11111111111")

    def setUp(self):
        RejestrKont.dodaj_konto(self.pierwsze_konto)

    def test_dodaj_konto_i_poprawna_liczba_rejestru(self):
        self.assertEqual(RejestrKont.pobierz_liczbe_kont(), 1)

    def test_znajdz_konto(self):
        self.assertEqual(RejestrKont.znajdz_konto("55072345789"), self.pierwsze_konto)

    def test_nie_znajdz_konta(self):
        self.assertEqual(RejestrKont.znajdz_konto("1"), None)

    def test_usun_konto(self):
        RejestrKont.dodaj_konto(self.drugie_konto)
        RejestrKont.usun_konto("55072345789")
        self.assertEqual(RejestrKont.rejestr, [self.drugie_konto])

    def test_zmien_konto(self):
        RejestrKont.zmien_konto("55072345789", "Ania", "Janosik")
        self.assertEqual(RejestrKont.rejestr[0].imie, "Ania")
        self.assertEqual(RejestrKont.rejestr[0].nazwisko, "Janosik")
    def test_zmien_konto_nie_dziala(self):
        self.assertEqual(RejestrKont.zmien_konto("55072345789"), None)
        self.assertEqual(RejestrKont.zmien_konto("55072", "Ania", "A"), None)

