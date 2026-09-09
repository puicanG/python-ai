import json

class User:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.nationality = "Romanian"

    def to_json(self):
        d1 = {'name': self.name, 'age': self.age, 'nationality': self.nationality}
        return json.dumps(d1)

    def say_hello(self):
        print(self.name + " says hello!")

    def __str__(self):
        return "" + self.name + " " + self.nationality + " " + str(self.age)


# folosind User() initializam o instanta a clasei User

sonia = User("Sonia", "30")
dragos = User("Dragos", "35")

dragos.age = 40
dragos.hobby = "Inginer"

print(dragos.to_json())

print(sonia)
print(dragos)

print(sonia.age)
print(sonia.nationality)

#structuri de date

#list: [10,20,30]
#dict: {"name": "adrian", "age" : 33}
#set, unordered list.

s1 = set([10,30,40,10])
print(s1)

# JSON

json_text = '{"name": "Jason", "age": 25}'
created_dict = json.loads(json_text)

print(created_dict["name"])
