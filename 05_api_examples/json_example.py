import json

json_data = '''
{
    "person": {
        "name": "Anna",
        "age": 24,
        "address": {
            "street": "Saarstraße 123",
            "city": "Mainz",
            "postalCode": "55122"
        },
        "hobbies": ["Lesen", "Radfahren", "Schwimmen"]
    }
}
'''

data = json.loads(json_data)

name = data["person"]["name"]
age = data["person"]["age"]
city = data["person"]["address"]["city"]
first_hobby = data["person"]["hobbies"][0]

print(f"Name: {name}")
print(f"Alter: {age}")
print(f"Stadt: {city}")
print(f"Erstes Hobby: {first_hobby}")