import requests


url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "foo",
    'body': "bar",
    "userid": 1
}

response = requests.post(url, data=data)

print(f"Статус кода - {response.status_code}")
print(f"Ответ - {response.json()}")





