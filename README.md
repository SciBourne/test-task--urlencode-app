[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![codecov](https://codecov.io/gh/SciBourne/test-task--urlencode-app/branch/main/graph/badge.svg?token=I122V71IIF)](https://codecov.io/gh/SciBourne/test-task--urlencode-app)
[![gitlab-ci: build](http://scibourne.gitlab.io/test-task-urlencode-app/build.svg)](https://gitlab.com/SciBourne/test-task-urlencode-app)
[![gitlab-ci: type-check](http://scibourne.gitlab.io/test-task-urlencode-app/type-check.svg)](https://gitlab.com/SciBourne/test-task-urlencode-app)
[![gitlab-ci: unit-tests](http://scibourne.gitlab.io/test-task-urlencode-app/unit-tests.svg)](https://gitlab.com/SciBourne/test-task-urlencode-app)
[![gitlab-ci: api-tests](http://scibourne.gitlab.io/test-task-urlencode-app/api-tests.svg)](https://gitlab.com/SciBourne/test-task-urlencode-app)

<br>

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
