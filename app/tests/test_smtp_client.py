from datetime import datetime
import unittest
from unittest.mock import MagicMock, patch

from app.SMTPClient import SMTPClient
from app.KontoPrywatne import KontoPrywatne
from app.KontoFirmowe import KontoFirmowe

class TestWysylkiHistoriiNaMail(unittest.TestCase):
    def setUp(self) -> None:
        self.pierwsze_konto = KontoPrywatne("Dariusz", "Januszewski", "21343234566435")
        self.przykladowa_historia = [-231, 123]
        self.pierwsze_konto.historia_przelewow = self.przykladowa_historia
        self.email = "email@gmail.com"

    def test_wysylki_mail_prywatne(self):
        smtp = SMTPClient()
        smtp.wyslij = MagicMock(return_value = True)
        
        konto = self.pierwsze_konto
        historia = self.pierwsze_konto.historia_przelewow
        temat = f"Wyciag z dnia {datetime.now().strftime('%Y-%m-%d')}"
        zawartosc = f"Twoja historia przelewow dla konta Prywatnego to: {historia}"

        odpowiedz = konto.wyslij_historie_na_mail(self.email, smtp)

        smtp.wyslij.assert_called_once()

        smtp.wyslij.assert_called_with(temat, zawartosc, self.email)
        self.assertTrue(odpowiedz)
        
    @patch("app.KontoFirmowe.KontoFirmowe.zapytanieDoMF")
    def test_wyslij_firmowa_historie_mail(self, mock):
        mock.return_value = True
        smtp = SMTPClient()
        smtp.wyslij = MagicMock(return_value = True)

        konto = KontoFirmowe("abc", "123")
        konto.historia_przelewow = self.przykladowa_historia
        historia = konto.historia_przelewow
        odpowiedz = konto.wyslij_historie_na_mail(self.email, smtp)

        temat = f"Wyciag z dnia {datetime.now().strftime('%Y-%m-%d')}"
        zawartosc = f"Twoja historia przelewow dla konta Firmowego to: {historia}"

        smtp.wyslij.assert_called_once()
        smtp.wyslij.assert_called_with(temat, zawartosc, self.email)
        self.assertTrue(odpowiedz)



