## Create DB for project
1. Install PostgreSQL.
2. Open PostgreSQL command line with command
   ```shell
   psql postgres
   ```
3. Create user
   ```SQL
   CREATE USER test WITH PASSWORD 'test';
   ```
4. Create Database
   ```SQL
   CREATE DATABASE test OWNER test;
   ```
5. Grant permission to user
   ```SQL
   GRANT ALL PRIVILEGES ON DATABASE test TO test;
   ```


## Setting Up project
1. Install Python 3.10 if not available on device
2. cd in the project repo
3. Create virtual env with python 3.10 with command
   ```shell
   python3.10 -m venv venv
   ```
4. Activate virtual env with command  
   ```shell
   source venv/bin/activate
   ```
5.  Install requirements with 
    ```shell
    pip install -r requirements.txt
    ```
6.  Migreate models
    ```shell
    python manage.py migrate
    ```
7.  Run Project with
    ```shell
    python manage.py runserver 0.0.0.0:8000
    ```



<br>
<br>

API Documentation
================

Introduction
------------
This document provides detailed information about the endpoints, request/response format, and error codes of the  API.

Endpoints
---------
The following endpoints are available in the API:

1. **Endpoint 1**
   - URL: `http://0.0.0.0:8000/user/`
   - Method: `POST`
   - Description: This endpoint used to add new user.
   - Request Format: Json
   - Request Example:
     ```json
     {
       "username": "username",
       "email": "user@gmail.com",
       "password": "pass"
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
     {
        "id": 2,
        "username": "username",
        "email": "user@gmail.com"
     }
     ```

2. **Endpoint 2**
   - URL: `http://0.0.0.0:8000/user/<id>`
   - Method: `GET`
   - Description: Get info of a user.
   - Response Format: JSON
   - Response Example:
     ```json
     {
        "id": 1,
        "username": "test",
        "email": "teset@gmail.com"
     }
     ```
    
3. **Endpoint 3**
   - URL: `http://0.0.0.0:8000/user/<id>/`
   - Method: `PATCH`
   - Description: Update info of a user.
   - Request Format: Json
   - Request Example:
     ```json
     {
       "email": "user@gmail.com",
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
     {
        "id": 1,
        "username": "test",
        "email": "user@gmail.com"
     }
     ```

4. **Endpoint 4**
   - URL: `http://0.0.0.0:8000/posts/`
   - Method: `POST`
   - Description: This endpoint used to add new post.
   - Request Format: Json
   - Request Example:
     ```json
     {
       "title": "title",
       "content": "content",
       "user": 1
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
     {
        "created": "05-07-2023 15:35",
        "updated": "05-07-2023 15:35",
        "user": 1,
        "title": "title",
        "content": "content"
    }
     ```

5. **Endpoint 5**
   - URL: `http://0.0.0.0:8000/posts/`
   - Method: `GET`
   - Description: List all the posts.
   - Response Format: JSON
   - Response Example:
     ```json
     [
        {   "id": 1,
            "created": "05-07-2023 15:35",
            "updated": "05-07-2023 15:35",
            "user": 1,
            "title": "title1",
            "content": "content1"
        },
        {
            "id": 2,
            "created": "05-07-2023 15:40",
            "updated": "05-07-2023 15:40",
            "user": 1,
            "title": "title2",
            "content": "content2"
        }
     ]
     ```

6. **Endpoint 6**
   - URL: `http://0.0.0.0:8000/posts/<id>`
   - Method: `DELETE`
   - Description: Delete a specific post.

7. **Endpoint 7**
   - URL: `http://0.0.0.0:8000/posts/<id>/`
   - Method: `PATCH`
   - Description: This endpoint used to edit a post.
   - Request Format: Json
   - Request Example:
     ```json
     {
       "content": "content5",
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
      {
        "created": "05-07-2023 15:35",
        "updated": "05-07-2023 15:35",
        "user": 1,
        "title": "title",
        "content": "content5"
      }
     ```

Error Codes
-----------
The API may return the following error codes:

- `400 Bad Request`: The request is invalid or missing required parameters.
- `404 Not Found`: The requested resource does not exist.
- `500 Internal Server Error`: An unexpected error occurred on the server.
