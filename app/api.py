from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoPrywatne import KontoPrywatne

app = Flask(__name__)  # python3 -m flask --app api.py run


@app.route("/app/konta/<pesel>/przelew", methods=["POST"])
def wykonaj_przelew_osobisty(pesel):
    data = request.get_json()
    print(f"Otrzymano request POST: {data}")
    znalezisko = RejestrKont.znajdz_konto(pesel)
    if znalezisko is None:
        return jsonify({"message": "Nie znaleziono konta!"}), 404
    else:
        wartosc = data["wartosc"]
        typ = data["typ"]
        saldo = znalezisko.saldo
        if typ not in ["ekspres", "wychodzacy", "przychodzacy"]:
            return jsonify({"message": "Niepoprawny typ przelewu"}), 422
        if wartosc <= 0:
            return jsonify({"message": "Kwota przelewu mniejsza lub rowna zero"}), 400
        if typ == "ekspres" or typ == "wychodzacy":
            if saldo < wartosc:
                return jsonify({"message": "Saldo konta mniejsze niz kwota przelewu"}), 422
            if typ == "wychodzacy":
                znalezisko.przelew_wychodzacy(wartosc)
            else:
                znalezisko.przelew_ekspres(wartosc)
            return jsonify({"message": "Zlecenie przyjeto do realizacji"}), 200
        elif typ == "przychodzacy":
            znalezisko.przelew_przychodzacy(wartosc)
            return jsonify({"message": "Zlecenie przyjeto do realizacji"}), 200


@app.route('/app/konta', methods=['POST'])
def stworz_konto_prywatne():
    data = request.get_json()
    print(f"Otrzymano request POST: {data}")

    konto = KontoPrywatne(data["imie"], data["nazwisko"], data["pesel"])
    dodaj = RejestrKont.dodaj_konto(konto)
    if dodaj is None:
        return jsonify(
            {"message": "Nie utworzono konta."}
        ), 409
    else:
        return jsonify(
            {"message": "Konto prywatne utworzone!"}
        ), 201


@app.route('/app/konta/liczba', methods=['GET'])
def wez_liczbe_kont():
    liczba_kont = RejestrKont.pobierz_liczbe_kont()
    return jsonify({
        "message": f"Liczba kont w rejestrze to {liczba_kont}!",
        "liczba": liczba_kont
    }), 200


@app.route('/app/konta/<pesel>', methods=['GET'])
def wez_konto_po_peselu(pesel):
    znalezisko = RejestrKont.znajdz_konto(str(pesel))
    if znalezisko is None:
        return jsonify({"message": "Nie znaleziono konta!"}), 404
    else:
        return jsonify(
            {"message": "Konto prywatne znalezione!",
             "imie": znalezisko.imie,
             "nazwisko": znalezisko.nazwisko,
             "pesel": znalezisko.pesel,
             "saldo": znalezisko.saldo, }
        ), 200


@app.route('/app/konta/<pesel>', methods=['DELETE'])
def usun_konto_po_peselu(pesel):
    znalezisko = RejestrKont.usun_konto(pesel)
    if znalezisko is None:
        return jsonify({"message": "Nie znaleziono konta!"}), 404
    else:
        return jsonify(
            {"message": "Konto prywatne usunieto!"}
        ), 200


@app.route('/app/konta/<pesel>', methods=['PATCH'])
def zmien_konto_po_peselu(pesel):
    data = request.get_json()
    print(f"Otrzymano request PATCH: {data}")

    try:
        imie = data["imie"]
    except KeyError:
        imie = None

    try:
        nazwisko = data["nazwisko"]
    except KeyError:
        nazwisko = None

    znalezisko = RejestrKont.zmien_konto(pesel, imie, nazwisko)
    if znalezisko is None:
        return jsonify({"message": "Nie znaleziono konta!"}), 404
    else:
        return jsonify(
            {"message": "Konto prywatne znalezione oraz zmienione!"}
        ), 200
