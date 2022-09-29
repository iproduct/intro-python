import json

if __name__ == '__main__':
    x = [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        }
    ]
    with open('db.json', 'wt', encoding='utf-8') as f:
        json.dump(x, f, indent=4)

    with open('db.json', 'rt', encoding='utf-8') as f:
        json_str = json.load(f)

    print(json_str)
