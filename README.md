# Тестовое задание

Написать эндпойнт, в качестве параметра принимающий незакодированную (unencoded) ссылку и возвращающий её закодированный вариант.

<br>

# API

Host:
```
127.0.0.1:8000
```
Entrypoint:
```
/api/v1
```

<br>

### Процентное кодирование

Request:
```http
GET /urlencode?encode_type=percent&source=http://yandex.ru HTTP/1.1
```
Response:
```json
{
  "encoded_url": "http%3A%2F%2Fyandex.ru",
  "encode_type": "percent"
}
```

<br>

### Кодирование base64

Request:
```http
GET /urlencode?encode_type=base64&source=http://yandex.ru HTTP/1.1
```
Response:
```json
{
  "encoded_url": "aHR0cDovL3lhbmRleC5ydQ==",
  "encode_type": "base64"
}
```

<br>

### Кодирование по-умолчанию (процентное)

Request:
```http
GET /urlencode?source=http://yandex.ru HTTP/1.1
```
Response:
```json
{
  "encoded_url": "http%3A%2F%2Fyandex.ru",
  "encode_type": "percent"
}
```
