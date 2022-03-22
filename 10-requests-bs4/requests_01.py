import requests

if __name__ == '__main__':
    r = requests.get('https://api.github.com/events')
    # for event in r.json():
    #     print(event)

    r = requests.get('https://docs.python-requests.org/en/latest/user/quickstart/')
    print(r.text[:1000])
