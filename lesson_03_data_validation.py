from typing import Literal

from pydantic import BaseModel,ValidationError, Field
from lesson_02_classes_objects import User

#mostenire. inheritage

class Address(BaseModel):
    street_address: str
    city: str


class UserValidator(BaseModel):
    name: str = Field(min_length=1, max_length=10)
    age: int = Field(ge=0, le=120, default=18)
    nationality: Literal["Romanian", "Moldovean"]
    external: bool | None = None
    adress: Address

received_user = {
    "name": "Vicenntiu",
    "age": 25,
    "nationality": "Romanian"
}
print("========Validations=========")

#try catch
try:
    validated_user = UserValidator.model_validate(received_user, strict=True)
    print(validated_user)
except ValidationError as e:
    print(e)
    print(e.errors)
finally:
    print("Validare completa")

varx = None
print(varx)

def function2():
    v = 10
    v += 20
    return None

