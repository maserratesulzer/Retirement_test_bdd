from pytest_bdd import scenario, given, when, then, parsers
from RetirementAge import retirement

EXTRA_TYPES = {'Number': int, 'String': str}
CONVERTERS = {'birth_year': int, 'years_old': int, 'months_old': int}


@scenario("retirement.feature", "The user enters a valid birth month", example_converters=CONVERTERS, features_base_dir="../features")
def test_add():
    pass


@given("the birth year")
def calc(year):
    return retirement(year)


@then("the user's retirement age will be the variables years_old, and months_old")
def validate(calc, years, months):
    assert calc == (years, months)
