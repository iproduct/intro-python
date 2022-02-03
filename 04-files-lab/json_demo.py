import json

from entity.user import User

if __name__ == '__main__':
    # l = [1, User(1, "Hristo", "Petrov", "hristo", "hristo123"),
    #      {"name": "Траян", "age": 22}, ("hello", "python")]
    l = [1, "hello", {"name": "Траян", "age": 22}, ("hello", "python")]
    s = json.dumps(l, indent=4, ensure_ascii= False)
    print(s)
    with open("sample.json", "wt", encoding="utf-8") as f:
        json.dump(l, f, indent=4, ensure_ascii= False)

    print(json.loads(s))
    with open("sample.json", "rt", encoding="utf-8") as f:
        print(json.load(f))