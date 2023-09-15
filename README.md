## About


REST API capable of CRUD operations on a person.

## Local Setup
- Clone the project repository from GitHub.
     ```json
     $ git clone <repository_url>
     ```
- Create A Virtualenvironment
     ```bash
     $ virtualenv env
     $ source env/bin/activate
     ```
- Install Dependencies

     ```python
     $ pip install -r requirements.txt
     ```
- Run database migrations.
    ```json
     $ python manage.py migrate
    ```
- Run Server
   ```python 
     $ python manage.py runserver
   ```

- Access the API at
   ```python 
     http://localhost:8000/api/v1/
   ```
## How To Use The API
#### Step 1: Register Auth User

```curl

curl --location --request POST 'http://localhost:8000/api/v1/user-create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test_user",
    "password": "test"
}'

```

```curl
response: {"id":"12457815-1cd7-4e47-b83c-7e1c530e5bfe","username":"test_user","first_name":"","last_name":"","email":"","auth_token":"cd2c5dc813d6a4c83d8032a1644b892f71653440"}
```

#### Step 2: Get Authentication Token

```curl

curl --location --request POST 'http://localhost:8000/api-token-auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test_user",
    "password": "test"
}'


```

```curl
response: cd2c5dc813d6a4c83d8032a1644b892f71653440
```

#### Step 3: Create Person
``` curl

curl --location --request POST 'http://localhost:8000/api/v1/person/' \
--header 'Authorization: Token cd2c5dc813d6a4c83d8032a1644b892f71653440' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Kamau",
    "value": "elon"
}'

```

```curl
response: {"id":2,"name":"Kamau","value":"elon"}
```


#### Step 4: Update Person

```curl

curl --location --request PUT 'http://localhost:8000/api/v1/person/1/' \
--header 'Authorization: Token cd2c5dc813d6a4c83d8032a1644b892f71653440' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Comrades",
    "value": "quickie"
}'

```

```curl
response: {"id":2,"name":"Comrades","value":"quickie"}
```


#### Step 5: Get Person

```curl

curl --location --request GET 'http://localhost:8000/api/v1/person/1/' \
--header 'Authorization: Token cd2c5dc813d6a4c83d8032a1644b892f71653440'

```

```curl
response: {"id":2,"name":"Comrades","value":"quickie"}
```

#### Step 6: Delete Person

```curl

curl --location --request DELETE 'http://localhost:8000/api/v1/person/1/' \
--header 'Authorization: Token cd2c5dc813d6a4c83d8032a1644b892f71653440'

```

```curl
response: 
```