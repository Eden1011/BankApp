class RejestrKont:
    rejestr = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.rejestr.append(konto)

    @classmethod
    def znajdz_konto(cls, pesel):
        for konto in cls.rejestr:
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def pobierz_liczbe_kont(cls):
        return len(cls.rejestr)

