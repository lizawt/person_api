## Person API Documentation

### Introduction
The Person API is a simple RESTful API for managing information about individuals. It provides endpoints for creating, retrieving, updating, and deleting person records.

### Base URL
The base URL for all API endpoints is /api/v1.


### Endpoints
#### 1. Create a Person
##### Endpoint:https://hngxstg2-qvjg.onrender.com/api/v1/person/
##### Method: POST

##### Request Body (JSON):

```json
{
    "name": "John Doe",
    "value": "The great",
}
```
##### Response (HTTP Status 201 Created):

```json
{
    "id": 1,
    "name": "John Doe",
    "value": "The great"
}
```

#### 2. Retrieve a Person by ID
##### Endpoint:https://hngxstg2-qvjg.onrender.com/api/v1/person/{id}/
##### Method: GET

##### Response (HTTP Status 200 OK):
```json
{
    "id": 1,
    "name": "John Doe",
    "value": "The great",
}
```

#### 3. Update a Person by ID
##### Endpoint:https://hngxstg2-qvjg.onrender.com/api/v1/person/{id}/
##### Method: PUT

##### Response (HTTP Status 200 OK):
```json
{
    "name": "Uhuru Ruto",
    "value": "Misleaders",
}
```

#### 4. Delete a Person by ID
##### Endpoint:https://hngxstg2-qvjg.onrender.com/api/v1/person/{id}/
##### Method: DELETE

##### Response (HTTP Status 204 No Content):
```json

```

### Limitations and Assumptions
It was assumed that all APIs should have some level of authentication.

The API assumes that the "name" field is unique, and there can be no two persons with the same name.

Validation is applied to ensure that the "name" field only accepts string values.




### Deployment

#### 👉 Create PostgreSQL database on render
- Go to https://dashboard.render.com/new/database this link.

- Database name and user should be the same as the one on render.yaml.

#### 👉 Create a Blueprint instance
- Go to https://dashboard.render.com/blueprints this link.

- Click New Blueprint Instance button.
Connect your repo which you want to deploy.

- Fill the Service Group Name and click on Update Existing Resources button.

- Connect your repo which you want to deploy.

- After that your deployment will start automatically.
