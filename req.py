import requests
import json

status ='available'

# Получение информации о питомцах

res_get = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})

print(f"Статус выполнения кода GET: {res_get.status_code}")
print(res_get.text)
print(res_get.json())
print(type(res_get.json()))


# Добавление нового питомца

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Dandy",
  "photoUrls": [
    "Dandy's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_post = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(info, ensure_ascii=False))

print(f"Статус выполнения кода POST: {res_post.status_code}")
print(res_post.text)
print(res_post.json())
print(type(res_post.json()))

# Изменение питомца

data1 = {
  "id": 9223372036854706225,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_put = requests.put(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(data1, ensure_ascii=False))

print(f"Статус выполнения кода PUT: {res_put.status_code}")
print(res_put.text)
print(res_put.json())
print(type(res_put.json()))

# Удаление питомца

petID = 9223372036854706225
res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{petID}', headers={'accept': 'application/json'})
print(f"Статус выполнения кода DELETE: {res_delete.status_code}")
print(res_delete.text)
print(res_delete.json())
print(type(res_delete.json()))



