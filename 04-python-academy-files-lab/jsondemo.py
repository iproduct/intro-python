import json

if __name__ == "__main__":
  person = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
      {"model": "BMW 230", "mpg": 27.00},
      {"model": "Ford Edge", "mpg": 24.1}
    ]
  }

  # convert into JSON:
  with open("person.json", "wt", encoding="utf-8") as f:
    json.dump(person, f, indent=4)

  # the result is a JSON string:
  with open("person.json", "rt", encoding="utf-8") as f:
    result = json.load(f)
    print(result)
    print(type(result['age']))