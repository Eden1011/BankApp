class Konto:
    def __init__(self):
        self.saldo = 0

    def przelew_przychodzacy(self, wartosc):
        if wartosc > 0:
            self.saldo += wartosc
        else:
            return self.saldo
    
    def przelew_wychodzacy(self, wartosc):
        if self.saldo > 0 and self.saldo >= wartosc:
            self.saldo -= wartosc
    def przelew_ekspres(self, wartosc):
        if self.saldo <= 0:
            return
        else:
            self.przelew_wychodzacy(wartosc)