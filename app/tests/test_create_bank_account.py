import unittest
from unittest.mock import mock_open, patch
import requests

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
        mock_zapytanieDoMF.assert_not_called()
    
    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=True)
    def test_tworzenie_konta_firmowego_poprawny_nip(self, mock_zapytanieDoMF):
        pierwsze_konto = KontoFirmowe("PLACEHOLDER", NIP="8461627561")
        self.assertEqual(pierwsze_konto.nip, "8461627561")
        mock_zapytanieDoMF.assert_called_once_with("8461627561")
    
    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF", return_value=False)
    def test_tworzenie_firmowe_niepoprawny_10_liczoby_nip_error(self, mock_zapytanieDoMF):
        with self.assertRaises(ValueError) as context:
            KontoFirmowe("PLACEHOLDER", NIP="1111111111")
        self.assertEqual(str(context.exception), "Firma nie zarejestrowana!")
        mock_zapytanieDoMF.assert_called_once_with("1111111111")
    
    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF")
    def test_zapytanie_DoMF(self, mock_zapytanieDoMF):
        mock_zapytanieDoMF.return_value = False
        self.assertFalse(KontoFirmowe.zapytanieDoMF("8461627560"))
        mock_zapytanieDoMF.assert_called_once_with("8461627560")

    @patch('app.KontoFirmowe.requests.get')
    @patch('app.KontoFirmowe.time.strftime', return_value='2023-06-14')
    def test_zapytanieDoMF_valid_nip(self, mock_strftime, mock_get):
        # Przygotowanie mocka
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Wywołanie testowanej funkcji
        result = KontoFirmowe.zapytanieDoMF("1234567890")

        # Sprawdzenie wyniku
        self.assertTrue(result)
        mock_get.assert_called_once_with("https://wl-api.mf.gov.pl/api/search/nip/1234567890?date=2023-06-14")

    @patch('app.KontoFirmowe.requests.get')
    @patch('app.KontoFirmowe.time.strftime', return_value='2023-06-14')
    def test_zapytanieDoMF_invalid_nip(self, mock_strftime, mock_get):
        # Przygotowanie mocka
        mock_response = requests.Response()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Wywołanie testowanej funkcji
        result = KontoFirmowe.zapytanieDoMF("1234567890")

        # Sprawdzenie wyniku
        self.assertFalse(result)
        mock_get.assert_called_once_with("https://wl-api.mf.gov.pl/api/search/nip/1234567890?date=2023-06-14")
