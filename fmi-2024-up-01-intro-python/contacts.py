import json

sample_contacts = [
    {
        "id": 1,
        "first": "Trayan",
        "last": "Iliev",
        "address": {
            "country": "BG",
            "city": "Sofia",
            "street": "Jamaes Bouchier Blvd., 42"
        },
        "phones": [
            {
                "type": "work",
                "number": "+3592895423"
            },
            {
                "type": "mobile",
                "number": "+359885167243"
            },
        ]
    },
    {
        "id": 2,
        "first": "Georgi",
        "last": "Spasov",
        "address": {
            "country": "BG",
            "city": "Plovdiv",
            "street": "Pet tepeta, 18"
        },
        "phones": [
            {
                "type": "work",
                "number": "+3594312345"
            },
            {
                "type": "mobile",
                "number": "+359889195572"
            },
        ]
    }
]

def format_contact(contact: dict) -> str:
    result = ''
    phones_str = ', '.join([f'{ph["type"]}: {ph["number"]}' for ph in contact['phones']])
    result += f'| {contact["id"]:>3d} | ' \
              f'{contact["first"] + " " + contact["last"]:<15.15s} | ' \
              f'{contact["address"]["street"] + ", " + contact["address"]["city"] + ", " + contact["address"]["country"]:<40.40s} | ' \
              f'{phones_str:40.40s} |'
    return result

def print_contacts(contacts):
    for contact in contacts:
        print(format_contact(contact))

if __name__ == "__main__":
    with open('contacts.json', 'wt', encoding='utf-8') as f:
        json.dump(sample_contacts, f, indent=4)

    with open('contacts.json', 'rt', encoding='utf-8') as f:
        contacts_list = json.load(f)
        print_contacts(contacts_list)