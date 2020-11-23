import pytest
from retirement import *
from retirement import _validate_age_month, _validate_age_year, _validate_birth_month

#Test the exeption when the month is not on the limits
def test_validate_month():

    with pytest.raises(ValueError):
        _validate_age_month(12)

#Test the exeption when the age is not on the limits
def test_validate_month2():
    with pytest.raises(ValueError):
        _validate_age_month(-1)

#Test the exeption when the age is not on the limits
def test_validate_age_year():
    age=64
    with pytest.raises(ValueError):
        _validate_age_year(age)

#Test the exeption when the age is not on the limits
def test_validate_birth_month():
    age = 64
    with pytest.raises(ValueError):
        _validate_birth_month(age)

def test_validate_birth_month2():
    month = 63
    with pytest.raises(ValueError):
        _validate_birth_month(month)

#Test the retirement age based on the year you were born
def test_calculate_retirement_age():
    age=1937
    assert calculate_retirement_age(1937)== (65,0)

def test_calculate_retirement_age():
    age=1940
    assert calculate_retirement_age(age)== (65,6)

#test the retirement age (year and month)
def test_calculate_retirement_date():
    birth_year=1940
    birth_mont=1
    age_years=65
    age_months=1
    assert calculate_retirement_date(birth_year,birth_mont,age_years,age_months)== (2005, 2)

#test the retirement age (year and month)
def test_calculate_retirement_date():
    birth_year=1941
    birth_mont=1
    age_years=65
    age_months=1
    assert calculate_retirement_date(birth_year,birth_mont,age_years,age_months)== (2006, 2)


#assert sorted_by_date(l) == l2