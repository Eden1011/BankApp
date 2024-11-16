import unittest

from parameterized import parameterized

from ..KontoPrywatne import KontoPrywatne as Konto
from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    def setUp(self):
        self.imie_nazwisko = ("Dariusz", "Januszewski")
        self.pierwsze_konto = Konto(*self.imie_nazwisko, "PLACE-HOLDER-404")
    @parameterized.expand([
        ("Poprawny pesel", "32154365499", "32154365499"),
        ("Niepoprawny pesel", "321", "Pesel nie jest poprawny!")])
    def test_tworzenie_konta(self, name, input, expected):
        self.pierwsze_konto.pesel = input #Aktywuje setter pesela w klasie KontoPrywatne
        self.assertEqual(self.pierwsze_konto.pesel, expected)
        self.assertEqual(self.pierwsze_konto.saldo, 0)
        self.assertEqual(self.pierwsze_konto.imie, self.imie_nazwisko[0])
        self.assertEqual(self.pierwsze_konto.nazwisko, self.imie_nazwisko[1])

    def test_wieku_oraz_promocji(self):
        #Poprawny pesel, z poprawnym rokiem, i poprawa promocja
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "82041523457"

        self.assertGreaterEqual(self.pierwsze_konto.rok, 1960)
        self.assertEqual(self.pierwsze_konto.promocja, "PROM_123")

        #Poprawna promocja, z niepoprawnym peselem
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "321"
        self.assertEqual(self.pierwsze_konto.rok, "Rok nie odpowiada promocji!")
        self.assertEqual(self.pierwsze_konto.promocja, "Promocja nie poprawna!")

        #Poprawna promocja, z poprawnym peselem, ale za malym wiekiem
        self.pierwsze_konto.promocja = "PROM_123"
        self.pierwsze_konto.pesel = "55072345789"
        self.assertEqual(self.pierwsze_konto.rok, "Rok nie odpowiada promocji!")
        self.assertEqual(self.pierwsze_konto.promocja, "Promocja nie poprawna!")

    @parameterized.expand([
        ("poprawny nip", 1234567890, 1234567890),
        ("niepoprawny nip", 1, "Niepoprawny NIP!")])
    def test_konto_firmowe(self, name, input, expected):
        self.konto_firmowe = KontoFirmowe("PLACEHOLDER", NIP=input)
        self.assertEqual(self.konto_firmowe.nip, expected)