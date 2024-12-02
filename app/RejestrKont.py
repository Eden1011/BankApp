class RejestrKont:
    rejestr = []
    liczba = 0

    @classmethod
    def dodaj_konto(cls, konto):
        for i in cls.rejestr:
            if i.pesel == konto.pesel:
                return None
        cls.rejestr.append(konto)
        cls.liczba += 1
        return konto

    @classmethod
    def znajdz_konto(cls, pesel):
        for konto in cls.rejestr:
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def pobierz_liczbe_kont(cls):
        return cls.liczba

    @classmethod
    def usun_konto(cls, pesel):
        znalezione = cls.znajdz_konto(pesel)
        if znalezione is not None:
            n_rejestr = []
            for i in cls.rejestr:
                if i != znalezione:
                    n_rejestr.append(i)
            cls.rejestr = n_rejestr
            cls.liczba -= 1
            return cls.rejestr
        else:
            return None

    @classmethod
    def zmien_konto(cls, pesel, imie=None, nazwisko=None):
        if imie is None and nazwisko is None:
            return None
        znalezione = cls.znajdz_konto(pesel)
        if znalezione is not None:
            cls.usun_konto(znalezione)
            konto = znalezione
            if imie is not None:
                konto.imie = imie
            if nazwisko is not None:
                konto.nazwisko = nazwisko
            cls.dodaj_konto(konto)
            return konto
        else:
            return None
