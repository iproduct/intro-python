import json
import requests

if __name__ == '__main__':
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    print(todos[:10])
    print(len(todos))