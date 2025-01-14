import unittest
from unittest.mock import mock_open, patch

from parameterized import parameterized

from ..KontoPrywatne import KontoPrywatne as Konto
from ..KontoFirmowe import KontoFirmowe


class TestCreateBankAccount(unittest.TestCase):
    def setUp(self):
        self.imie_nazwisko = ("Dariusz", "Januszewski")
        self.pierwsze_konto = Konto(*self.imie_nazwisko, "PLACE-HOLDER-404")

    @parameterized.expand(
        [("Poprawny pesel", "32154365499", "32154365499"), ("Niepoprawny pesel", "321", "Pesel nie jest poprawny!")])
    def test_tworzenie_konta(self, name, input, expected):
        self.pierwsze_konto.pesel = input  # Aktywuje setter pesela w klasie KontoPrywatne
        self.assertEqual(self.pierwsze_konto.pesel, expected)
        self.assertEqual(self.pierwsze_konto.saldo, 0)
        self.assertEqual(self.pierwsze_konto.imie, self.imie_nazwisko[0])
        self.assertEqual(self.pierwsze_konto.nazwisko, self.imie_nazwisko[1])

    def test_wieku_oraz_promocji(self):
        # Poprawny pesel, z poprawnym rokiem, i poprawa promocja
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "82041523457"

        self.assertGreaterEqual(self.pierwsze_konto.rok, 1960)
        self.assertEqual(self.pierwsze_konto.promocja, "PROM_123")

        # Poprawna promocja, z niepoprawnym peselem
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "321"
        self.assertEqual(self.pierwsze_konto.rok, "Rok nie odpowiada promocji!")
        self.assertEqual(self.pierwsze_konto.promocja, "Promocja nie poprawna!")

        # Poprawna promocja, z poprawnym peselem, ale za malym wiekiem
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "55072345789"
        self.assertEqual(self.pierwsze_konto.rok, "Rok nie odpowiada promocji!")
        self.assertEqual(self.pierwsze_konto.promocja, "Promocja nie poprawna!")

    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=False)
    def test_tworzenie_konta_firmowego_niepoprawny_nip(self, mock_zapytanieDoMF):
        pierwsze_konto = KontoFirmowe("PLACEHOLDER", NIP="5431243")
        self.assertEqual(pierwsze_konto.nip, "Niepoprawny NIP!")

    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=True)
    def test_tworzenie_konta_firmowego_poprawny_nip(self, mock_zapytanieDoMF):
        pierwsze_konto = KontoFirmowe("PLACEHOLDER", NIP="8461627561")
        self.assertEqual(pierwsze_konto.nip, "8461627561")

    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=False)
    def test_tworzenie_firmowe_niepoprawny_10_liczoby_nip_error(self, mock_zapytanieDoMF):
        with self.assertRaises(ValueError) as context:
            pierwsze_konto = KontoFirmowe("PLACEHOLDER", NIP="1111111111")
        self.assertEqual(str(context.exception), "Firma nie zarejestrowana!")

    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=False)
    def test_zapytanie_DoMF(self, mock_zapytanieDoMF):
        self.assertEqual(KontoFirmowe.zapytanieDoMF("8461627560"), False)
