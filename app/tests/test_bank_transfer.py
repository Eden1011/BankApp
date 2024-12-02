import unittest

from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe
from ..KontoPrywatne import KontoPrywatne as Konto


class TestPrzelewBankAccount(unittest.TestCase):

    def setUp(self):
        self.pierwsze_konto = Konto("Dariusz", "Januszewski", "82151166666")
        self.konto_firmowe = KontoFirmowe("Dariusz", "1234567890")

    # Edge case przelewu przychodzacego
    def test_czy_da_sie_odebrac_zerowy_przelew(self):
        self.stare_Saldo = self.pierwsze_konto.saldo
        self.pierwsze_konto.przelew_przychodzacy(0)
        self.assertEqual(self.stare_Saldo + 0, self.pierwsze_konto.saldo)

    # Standardowy test jednorazowy dla przelewu przychodzacego
    def test_czy_przelew_przychodzacy_dziala(self):
        self.stare_Saldo = self.pierwsze_konto.saldo
        self.pierwsze_konto.przelew_przychodzacy(50)
        self.assertEqual(self.stare_Saldo + 50, self.pierwsze_konto.saldo)

    def test_czy_przelew_wychodzacy_dziala(self):
        self.pierwsze_konto.saldo = 100
        self.stare_saldo = self.pierwsze_konto.saldo

        self.pierwsze_konto.przelew_wychodzacy(50)
        self.assertEqual(self.stare_saldo - 50, self.pierwsze_konto.saldo, "Saldo konta nie jest poprawne")

    def test_czy_przelew_wychodzacy_niedziala(self):
        self.pierwsze_konto.saldo = 10
        self.stare_saldo = self.pierwsze_konto.saldo
        self.pierwsze_konto.przelew_wychodzacy(50)
        self.assertEqual(self.pierwsze_konto.saldo, self.stare_saldo, "Saldo konta nie jest poprawne")

    def test_oplaty_zaksiegowania_dla_firm(self):
        self.konto_firmowe.saldo = 51
        self.konto_firmowe.przelew_ekspres(50)
        self.assertEqual(self.konto_firmowe.saldo, -4, "Saldo konta nie jest poprawne")

    def test_czy_mozna_wysylac_przelewy_z_ujemnym_saldem(self):
        self.konto_firmowe.saldo = -5
        self.konto_firmowe.przelew_ekspres(50)
        self.assertEqual(self.konto_firmowe.saldo, -5, "Saldo konta nie jest poprawne")

    def test_czy_mozna_wysylac_przelewy_z_ujemnym_saldem_dla_kont_prywatnych(self):
        self.pierwsze_konto.saldo = -1
        self.pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(self.pierwsze_konto.saldo, -1, "Saldo konta nie jest poprawne")

    def test_roznica_w_saldzie_dla_konta_prywatnego(self):
        self.pierwsze_konto.saldo = 50
        self.pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(self.pierwsze_konto.saldo, -1, "Saldo konta nie jest poprawne")

    def test_historii_przelewow_wychodzacych(self):
        self.pierwsze_konto.saldo = 50
        self.pierwsze_konto.przelew_ekspres(50)
        self.assertEqual(self.pierwsze_konto.historia_przelewow, [-50, -1], "Historia przelewow nie jest poprawna!")

    def test_historii_przelewow_przychodzacych(self):
        self.pierwsze_konto.przelew_przychodzacy(50)
        self.assertEqual(self.pierwsze_konto.historia_przelewow, [50], "Historia przelewow nie jest poprawna!")
