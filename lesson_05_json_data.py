import json
from lesson_03_data_validation import UserValidator



if __name__ == "__main__":
    with open("user_data.json", "r") as f:
        #json.loads() - deserializeaza un string din format Json in object python
        #json.Load(f) - deserializeaza un fiser care contine information Json in object python
            data = json.load(f)
            validated_user = UserValidator.model_validate(data, strict=True)
            print(validated_user)