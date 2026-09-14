import pydantic
import pytest
from lesson_03_data_validation import UserValidator

def test_simple_1():
    var1 = 10
    assert var1 <= 20
    assert var1 == 10


def test_user_validation():
    received_user = {
        "name": "Vicenntiu",
        "age": 25,
        "nationality": "Romanian",
        "adress": {
            "city": "Brasov",
            "street": "Principala"
        }
    }
    user = UserValidator.model_validate(received_user, strict = True  )

    assert isinstance(user, UserValidator)
    assert len(user.name) <=10 and len(user.name) >= 2
    assert isinstance(user.name, str)
    assert isinstance(user.nationality, str)
    assert isinstance(user.age, int)


def test_invalid_user():
    user_data = {
        "name": "Vicentiu",
        "age": 25,
        "nationality": "Romanian",
        "adress": {
            "city": "Brasov",
            "street": "Principala"
        }
    }

#decorator
@pytest.mark.parametrize("age", [-1, 130, 500, 1000])
def test_user_age_validation(age):
    with pytest.raises(pydantic.ValidationError):
        received_user = {
        "name": "Vicenntiu",
        "age": age,
        "nationality": "Romanian",
        "adress": {
            "city": "Brasov",
            "street": "Principala"
                  }
         }
    user = UserValidator.model_validate(received_user, strict = True )