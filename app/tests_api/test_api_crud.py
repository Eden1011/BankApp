import unittest, requests

class TestApiCrud(unittest.TestCase):
    def setUp(self):
        self.user = {
            "imie": "Dariusz",
            "nazwisko": "Januszewski",
            "pesel": "11111111111"
        }
    def test_stworz_konto(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        self.assertEqual(odp.status_code, 201)
        self.assertEqual(odp.json()["message"], "Konto prywatne utworzone!")


    def test_wez_liczbe_konto(self):
        odp = requests.get("http://localhost:5000/app/konta/liczba")
        self.assertEqual(odp.status_code, 200)

    def test_znajdz_dobre_konto(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.get(f"http://localhost:5000/app/konta/{self.user['pesel']}")
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Konto prywatne znalezione!")
        self.assertEqual(odp.json()["imie"], "Nowe_Imie")
        self.assertEqual(odp.json()["nazwisko"], self.user["nazwisko"])
        self.assertEqual(odp.json()["pesel"], self.user["pesel"])
        self.assertEqual(odp.json()["saldo"], 0)

    def test_znajdz_zle_konto(self):
        odp = requests.get("http://localhost:5000/app/konta/0")
        self.assertEqual(odp.status_code, 404)
        self.assertEqual(odp.json()["message"], "Nie znaleziono konta!")

    def test_zmien_konto(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.patch(f"http://localhost:5000/app/konta/{self.user['pesel']}",
                             json={"imie": "Nowe_Imie"})
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Konto prywatne znalezione oraz zmienione!")

    def test_zle_zmien_konto(self):
        odp = requests.delete("http://localhost:5000/app/konta/0", json={"imie": "Nowe_Imie"})
        self.assertEqual(odp.status_code, 404)
        self.assertEqual(odp.json()["message"], "Nie znaleziono konta!")

    def test_usun_konto(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Konto prywatne usunieto!")
