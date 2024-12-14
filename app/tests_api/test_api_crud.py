import unittest, requests


class TestApiCrud(unittest.TestCase):
    def setUp(self):
        self.user = {"imie": "Dariusz", "nazwisko": "Januszewski", "pesel": "11111111111"}

    def test_przelew_osobisty_nie_ma_konta(self):
        odp = requests.post("http://localhost:5000/app/konta/0/przelew", json={
            "typ": "przychodzacy",
            "wartosc": 200,
        })
        self.assertEqual(odp.status_code, 404)
        self.assertEqual(odp.json()["message"], "Nie znaleziono konta!")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_przelew_osobisty_nie_ma_srodkow(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "wychodzacy",
            "wartosc": 200,
        })
        self.assertEqual(odp.status_code, 422)
        self.assertEqual(odp.json()["message"], "Saldo konta mniejsze niz kwota przelewu")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_kwota_przelewu_osobisty_0_wartosc(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "przychodzacy",
            "wartosc": 0,
        })
        self.assertEqual(odp.status_code, 400)
        self.assertEqual(odp.json()["message"], "Kwota przelewu mniejsza lub rowna zero")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_przelew_typ_nie_jest_znany(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "abcef",
            "wartosc": 100,
        })
        self.assertEqual(odp.status_code, 422)
        self.assertEqual(odp.json()["message"], "Niepoprawny typ przelewu")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_przelew_os_wych_ok(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "przychodzacy",
            "wartosc": 100,
        })
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "ekspres",
            "wartosc": 100,
        })
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Zlecenie przyjeto do realizacji")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_przelew_os_przych_ok(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        odp = requests.post(f"http://localhost:5000/app/konta/{self.user['pesel']}/przelew", json={
            "typ": "przychodzacy",
            "wartosc": 100,
        })
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Zlecenie przyjeto do realizacji")
        requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")

    def test_stworz_konto(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        self.assertEqual(odp.status_code, 201)
        self.assertEqual(odp.json()["message"], "Konto prywatne utworzone!")

    def test_stworz_konto_ale_ten_sam_pesel(self):
        odp = requests.post("http://localhost:5000/app/konta", json=self.user)
        self.assertEqual(odp.status_code, 409)
        self.assertEqual(odp.json()["message"], "Nie utworzono konta.")

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
        odp = requests.patch(f"http://localhost:5000/app/konta/{self.user['pesel']}", json={"imie": "Nowe_Imie"})
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Konto prywatne znalezione oraz zmienione!")

    def test_zle_zmien_konto(self):
        odp = requests.delete("http://localhost:5000/app/konta/0", json={"imie": "Nowe_Imie"})
        self.assertEqual(odp.status_code, 404)
        self.assertEqual(odp.json()["message"], "Nie znaleziono konta!")

    def test_usun_konto(self):
        odp = requests.delete(f"http://localhost:5000/app/konta/{self.user['pesel']}")
        self.assertEqual(odp.status_code, 200)
        self.assertEqual(odp.json()["message"], "Konto prywatne usunieto!")
