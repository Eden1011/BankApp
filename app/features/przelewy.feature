Feature: Przelewy bankowe

  Background:
    Given Konto z peselem "89092909876" istnieje w rejestrze
    And Konto z peselem "90010112345" istnieje w rejestrze

  Scenario: Udany przelew wychodzący
    Given Konto z peselem "89092909876" ma saldo 1000 PLN
    When Wykonuję przelew wychodzący na kwotę 100 PLN z konta o peselu "89092909876" na konto o peselu "90010112345"
    Then Konto z peselem "89092909876" powinno mieć saldo 900 PLN
    And Konto z peselem "90010112345" powinno mieć saldo 100 PLN

  Scenario: Niewystarczające środki na przelew wychodzący
    Given Konto z peselem "89092909876" ma saldo 50 PLN
    When Wykonuję przelew wychodzący na kwotę 100 PLN z konta o peselu "89092909876" na konto o peselu "90010112345"
    Then Powinienem zobaczyć komunikat błędu "Saldo konta mniejsze niz kwota przelewu"
    And Konto z peselem "89092909876" powinno mieć saldo 50 PLN
    And Konto z peselem "90010112345" powinno mieć saldo 0 PLN

  Scenario: Udany przelew przychodzący
    Given Konto z peselem "89092909876" ma saldo 1000 PLN
    When Wykonuję przelew przychodzący na kwotę 100 PLN na konto o peselu "89092909876"
    Then Konto z peselem "89092909876" powinno mieć saldo 1100 PLN

  Scenario: Udany przelew ekspresowy
    Given Konto z peselem "89092909876" ma saldo 1000 PLN
    When Wykonuję przelew ekspresowy na kwotę 100 PLN z konta o peselu "89092909876" na konto o peselu "90010112345"
    Then Konto z peselem "89092909876" powinno mieć saldo 899 PLN
    And Konto z peselem "90010112345" powinno mieć saldo 100 PLN

  Scenario: Niewystarczające środki na przelew ekspresowy
    Given Konto z peselem "89092909876" ma saldo 50 PLN
    When Wykonuję przelew ekspresowy na kwotę 100 PLN z konta o peselu "89092909876" na konto o peselu "90010112345"
    Then Powinienem zobaczyć komunikat błędu "Saldo konta mniejsze niz kwota przelewu"
    And Konto z peselem "89092909876" powinno mieć saldo 50 PLN
    And Konto z peselem "90010112345" powinno mieć saldo 0 PLN
