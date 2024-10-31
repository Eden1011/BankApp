class Konto:
    def __init__(self):
        self.saldo = 0

    def przelew_przychodzacy(self, wartosc):
        self.saldo += wartosc
    
    def przelew_wychodzacy(self, wartosc):
        if self.saldo >= wartosc:
            self.saldo -= wartosc
