## Create DB for the project
1. Install PostgreSQL.
2. Open the PostgreSQL command line with a command
   ```shell
   psql postgres
   ```
3. Create a user
   ```SQL
   CREATE USER test WITH PASSWORD 'test';
   ```
4. Create a Database
   ```SQL
   CREATE DATABASE test OWNER test;
   ```
5. Grant permission to the user
   ```SQL
   GRANT ALL PRIVILEGES ON DATABASE test TO test;
   ```
6. Install Redis if not installed on the system.
7. Start the Redis server 
   1. for Linux
      ```shell
      sudo systemctl start redis-server.service
      ```
   2. for mac
      ```shell
      brew services start redis
      ```


## Setting Up project
1. Install Python 3.10 if not available on the device
2. cd in the project repo
3. Create virtual env with Python 3.10 with the command
   ```shell
   python3.10 -m venv venv
   ```
4. Activate virtual env with the command  
   ```shell
   source venv/bin/activate
   ```
5.  Install requirements with 
    ```shell
    pip install -r requirements.txt
    ```
6.  Migrate models
    ```shell
    python manage.py migrate
    ```
7.  Run the Project with
    ```shell
    python manage.py runserver 0.0.0.0:8000
    ```



<br>
<br>

API Documentation
================

Introduction
------------
This document provides detailed information about the endpoints, request/response format, and API error codes.

Endpoints
---------
The following endpoints are available in the API:

1. **Endpoint 1**
   - URL: `http://0.0.0.0:8000/user/`
   - Method: `POST`
   - Description: This endpoint is used to add new users.
   - Request Format: JSON
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
   - Description: Get info about the user.
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
   - Request Format: JSON
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
   - Description: This endpoint is used to add new posts.
   - Request Format: JSON
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
   - Description: This endpoint is used to edit a post.
   - Request Format: JSON
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

8. **Endpoint 8**
   - URL: `http://0.0.0.0:8000/posts/<id>/like_post`
   - Method: `GET`
   - Description: This endpoint is used to add like to a post.
   - Request Format: JSON
   - Request Example:
     ```json
     {
       "user": 1,
       "like": "true"
     }
     ```
     ```json
     {
       "user": 1,
       "like": "false"
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
      {
       "Data": "Post Disliked"
      }
     ```
     ```json
      {
       "Data": "Post Liked"
      }
     ```

9. **Endpoint 9**
   - URL: `http://0.0.0.0:8000/posts/<id>/list_liked_by`
   - Method: `GET`
   - Description: This endpoint is for listing users who liked the post.
   - Response Format: JSON
   - Response Example:
     ```json
      [
         {
            "id": 2,
            "username": "test1",
            "email": "user2@mail.com"
         },
         {
            "id": 3,
            "username": "test2",
            "email": "user3@mail.com"
         }
      ]
     ```

10. **Endpoint 10**
   - URL: `http://0.0.0.0:8000/user/<id>/add_follower`
   - Method: `GET`
   - Description: This endpoint is used to add followers.
   - Request Format: JSON
   - Request Example:
     ```json
     {
       "follower": 2
     }
     ```
   - Response Format: JSON
   - Response Example:
     ```json
      {
         "Following": {
            "follower": 1,
            "following": 2
         }
      }
     ```

11. **Endpoint 11**
   - URL: `http://0.0.0.0:8000/user/<id>/list_follower`
   - Method: `GET`
   - Description: This endpoint is for listing followers.
   - Response Format: JSON
   - Response Example:
     ```json
      [
         {
            "id": 2,
            "username": "test1",
            "email": "user2@mail.com"
         },
         {
            "id": 3,
            "username": "test2",
            "email": "user3@mail.com"
         }
      ]
     ```

12. **Endpoint 12**
   - URL: `http://0.0.0.0:8000/user/<id>/list_following`
   - Method: `GET`
   - Description: This endpoint is for listing who the user is following.
   - Response Format: JSON
   - Response Example:
     ```json
      [
         {
            "id": 2,
            "username": "test1",
            "email": "user2@mail.com"
         },
         {
            "id": 3,
            "username": "test2",
            "email": "user3@mail.com"
         }
      ]
     ```

13. **Endpoint 13**
   - URL: `http://0.0.0.0:8000/user/<id>/list_liked_posts`
   - Method: `GET`
   - Description: This endpoint is for listing posts liked by the user
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

Error Codes
-----------
The API may return the following error codes:

- `400 Bad Request`: The request is invalid or missing the required parameters.
- `404 Not Found`: The requested resource does not exist.
- `500 Internal Server Error`: An unexpected error occurred on the server.
