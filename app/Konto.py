from datetime import datetime

class Konto:
    def __init__(self):
        self.saldo = 0
        self.historia_przelewow = []
        self.wstep_do_Mail = "Twoja historia przelewow to:"

    def przelew_przychodzacy(self, wartosc):
        if wartosc > 0:
            self.saldo += wartosc
            self.historia_przelewow.append(wartosc)
        else:
            return self.saldo

    def przelew_wychodzacy(self, wartosc):
        if self.saldo > 0 and self.saldo >= wartosc:
            self.saldo -= wartosc
            self.historia_przelewow.append(-wartosc)

    def przelew_ekspres(self, wartosc):
        if self.saldo <= 0:
            return
        else:
            self.przelew_wychodzacy(wartosc)

    def wyslij_historie_na_mail(self, email, instancjaSMTPClient):
        temat_Mail = f"Wyciag z dnia {datetime.now().strftime('%Y-%m-%d')}"
        zawartosc = f"{self.wstep_do_Mail} {str(self.historia_przelewow)}"
        return instancjaSMTPClient.wyslij(temat_Mail, zawartosc, email)
