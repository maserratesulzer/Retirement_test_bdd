from pytest_bdd import scenario, given, when, then, parsers
from RetirementAge import retirement

EXTRA_TYPES = {'Number': int, 'String': str}
CONVERTERS = {'birth_year': int, 'years_old': int, 'months_old': int}


@scenario("retirement.feature", "user will input a valid birth month", example_converters=CONVERTERS, features_base_dir="/home/travis/build/maserratesulzer/Retirement_test_bdd/tests/features")
def test_add():
    pass


@given("the birth year")
def calc(birth_year,months_old):
    return retirement(birth_year,months_old)


@then("the user's retirement age will be the variables years_old, and months_old")
def validate(calc, years_old, months_old):
    assert calc == (years_old, months_old)
