import pytest
from pytest_bdd import scenarios, given, when, then
from retirement import _validate_age_month


@scenarios('../features/retirement.feature', 'simple Month validation for retirement age program')
def test_add():
    pass


@given("a month for a retirement age calculation")
def step_month():
    # raise NotImplementedError(u'STEP: Given a month for a retirement age calculation')
    return 12


@when("the month value is entered Then the program checks if the value is a valid month between 1 and 12")
def step_impl(month):
    return _validate_age_month(month)


@then("the program checks if the value is a valid month between 1 and 12")
def step_impl2(x):
    assert x == 12
