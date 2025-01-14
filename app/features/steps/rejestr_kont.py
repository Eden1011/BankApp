from behave import *
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000/app"

@when('I create an account using name: "{imie}", last name: "{nazwisko}", pesel: "{pesel}"')
def create_account(context, imie, nazwisko, pesel):
    json_body = {
        "imie": f"{imie}",
        "nazwisko": f"{nazwisko}", 
        "pesel": pesel
    }
    create_resp = requests.post(URL + "/konta", json=json_body)
    assert_equal(create_resp.status_code, 201)

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/konta/liczba")
    assert_equal(response.status_code, 200)
    assert_equal(str(response.json()["liczba"]), count)

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 200)

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 404)

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 200)

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["imie", "nazwisko"]:
        raise ValueError(f"Invalid field: {field}. Must be 'imie' or 'nazwisko'.")
    json_body = {f"{field}": f"{value}"}
    response = requests.patch(URL + f"/konta/{pesel}", json=json_body)
    assert_equal(response.status_code, 200)

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/konta/{pesel}")
    assert_equal(response.status_code, 200)
    assert_equal(response.json()[field], value)
