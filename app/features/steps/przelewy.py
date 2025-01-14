from behave import *
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000/app"

@given('Konto z peselem "{pesel}" istnieje w rejestrze')
def account_exists(context, pesel):
    response = requests.get(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 200)

@given('Konto z peselem "{pesel}" ma saldo {amount} PLN')
def set_account_balance(context, pesel, amount):
    response = requests.patch(URL + f"/konta/{pesel}", json={"saldo": int(amount)})
    assert_equal(response.status_code, 200)

@when('Wykonuję przelew wychodzący na kwotę {amount} PLN z konta o peselu "{from_pesel}" na konto o peselu "{to_pesel}"')
def make_outgoing_transfer(context, amount, from_pesel, to_pesel):
    json_body = {
        "typ": "wychodzacy",
        "wartosc": int(amount)
    }
    response = requests.post(URL + f"/konta/{from_pesel}/przelew", json=json_body)
    context.response = response

@when('Wykonuję przelew przychodzący na kwotę {amount} PLN na konto o peselu "{pesel}"')
def make_incoming_transfer(context, amount, pesel):
    json_body = {
        "typ": "przychodzacy",
        "wartosc": int(amount)
    }
    response = requests.post(URL + f"/konta/{pesel}/przelew", json=json_body)
    context.response = response

@when('Wykonuję przelew ekspresowy na kwotę {amount} PLN z konta o peselu "{from_pesel}" na konto o peselu "{to_pesel}"')
def make_express_transfer(context, amount, from_pesel, to_pesel):
    json_body = {
        "typ": "ekspres",
        "wartosc": int(amount)
    }
    response = requests.post(URL + f"/konta/{from_pesel}/przelew", json=json_body)
    context.response = response

@then('Konto z peselem "{pesel}" powinno mieć saldo {amount} PLN')
def check_account_balance(context, pesel, amount):
    response = requests.get(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 200)
    assert_equal(response.json()["saldo"], int(amount))

@then('Powinienem zobaczyć komunikat błędu "{message}"')
def check_error_message(context, message):
    assert_equal(context.response.status_code, 422)
    assert_equal(context.response.json()["message"], message)
