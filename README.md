# Castr

## Introduction
The purpose of this project is to demonstrate proficiency in a number of skills relating to full-stack web development. These include database ORM's, RESTful API's, authorization through Auth0, and deployment through heroku.

### Dependencies
This project runs on the following programs: Python 3, PostgreSQL (database), `psycopg2` (database adapter), `SQLAlchemy` (SQL toolkit and ORM manager), `Flask`, and the `Flask-SQLAlchemy` extension. 

I've also used `Flask-Migrate` and `Flask-Script` to manage data migrations, `Flask-Cors` to manage CORS, and have chosen to include `python-dotenv` to simplify running the program. See `requirements.txt` for a full list.

## Getting Started
The API is hosted at https://castr-capstone-app.herokuapp.com/

#### Authentication
Castr uses Auth0 to handle its authentication and authorization, through permission-based roles. To demonstrate these roles, with their differing levels of access, I have provided three testing login's.

- Executive Producer
  - Login: executive_producer@agency.fsnd
  - Password: WIOEBFV9734IUAPEBF984HGT*
  - Permissions: Executive producers may view, add, edit, and delete actors and movies.
  - JWT Token: 
  ```
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg
  ```

- Casting Director
  - Login: casting_director@agency.fsnd
  - Password: jnfvbiuew98ejkvoidfdvzioo9e9e!
  - Permissions: Casting directors may view, add, update, and delete actors. They may also view and update movies, but they may NOT add or delete movies.
  - JWT Token:
  ```
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDRiYjJhNDRlYjAwNjkwNDdlMTEiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTI5NzEsImV4cCI6MTY0NTY3OTM3MSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.4T-DwfY9VopK5-YY-89lb13-6Gx0wTad4sxIrF68iprORfWxLPvXfm6yeJDIJZX9jl1MH9ab-rETfyX4QihX1ejGfvTxWHhmyMkLxbVKFWVRI5knrrkuQ6uQ3hkocU17_3P5BuPmul5ep3ENAqkzzVuXmvpnnHQSibyAplzmNvigjOepjWH6yZW-J8o5U6PUa5OaF48FIhmBP49DBIHwQTPtnLwvMoXSR70wy98tnsZ5orWEvX0Ft5lKfsY4Vb4g7Uc-KzcHmWtKbVNLkSoWfrCH2g6G-5TqQQsD7ltMem9QDhmpR-wdM1ycTUDI-WY7Tz49PnchhGSNg9mIWkXvAQ
  ```

- Casting Assistant
  - Login: casting_assistant@agency.fsnd
  - Password: diebpgbiapsgnoag98!
  - Permissions: Casting assistants may only view actors and movies. They may not add, edit, or delete actors or movies.
  - JWT Token:
  ```
  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDNjZGE3OGI3YTAwNzA2YmU2ZGUiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMxMDAsImV4cCI6MTY0NTY3OTUwMCwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.S6I6EouybzXh9Oi-kkg8wp7AyPr9MTfSMUSxVcDu1SzSLiYwlJWygUJm6SHcuu1-gUYr3fMkj_vY5T4GEs_oyv4zP7oV7-aHws7gtY5cKwOuEemEB1UELlSMazpwzwzdE-LX20B5sZwPRUmYVKYseD97XVrDY6z9xjeKio-T35tWsSe7gpCx5wbWmPvqoev4MegHlcizmMuAKmcChCwWbmvoCSVyuLms1ZrN2m2FHNHO1rk_3IVQQfzwcRA3_erfZf3XfewsV_4B3Kk2qc1YJA271gNUDWdwnqrBUPnjXlemZUUWKZZMnr5uSB88x_UmyudTxCTi5mlfxZV1AjTRwQ
  ```

**Please note** these tokens will expire. If they expire and you still need them to test this app through curl requests or the `test_castr.py` file provided, please use [this link](https://coffeeshop-fsnd-udacity.us.auth0.com/authorize?audience=castr-api&response_type=token&client_id=V3uevhfWxrarlXhyuQ4r0oBST6izmYF3&redirect_uri=http://localhost:3000) to get fresh JWT tokens and substitute them where appropriate.

This app stores tokens in browser memory, as opposed to local storage (which is not recommended). For this reason, peristence across page refreshes and browser tabs is not supported. Please see [this Auth0 page](https://auth0.com/docs/secure/security-guidance/data-security/token-storage?_ga=2.171840608.1376781327.1645584179-891335330.1645584179&_gl=1*1s6u40r*rollup_ga*ODkxMzM1MzMwLjE2NDU1ODQxNzk.*rollup_ga_F1G3E656YZ*MTY0NTU5MjQ2OC4yLjEuMTY0NTU5MjU3NC40MQ..#single-page-app-scenarios) for more information.

## API Reference

#### Endpoints

###### GET /actors
This endpoint returns all actors in the database.
- Requires `get:actors` permission.
- Arguments
  - Authorization header bearer token, data-type String.
- Sample Request:
```
curl -X GET https://castr-capstone-app.herokuapp.com/actors  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "actors":
    [
        {"age":60,"gender":"Nonbinary","id":10,"name":"Big Bird"},
        {"age":72,"gender":"female","id":44,"name":"Sigourney Weaver"},
        {"age":55,"gender":"female","id":45,"name":"Halle Berry"}
    ],
    "success":true
}
```

###### GET /movies
Similarly, this endpoint returns all movies in the database.
- Requires `get:movies` permission.
- Arguments
  - Authorization header bearer token, data-type String.
- Sample Request:
```
curl -X GET https://castr-capstone-app.herokuapp.com/movies  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "movies":
    [
        {"id":25,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Star Wars"},
        {"id":23,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Jaws"}
    ],
    "success":true
}
```

###### GET /actors/id
Returns only the actor whose ID matches the one provided.
- Requires `get:actors` permission.
- Arguments 
  - Actor ID (data-type integer,) at the end of the endpoint.
  - Authorization header bearer token (data-type String.)
- Sample Request:
```
curl -X GET https://castr-capstone-app.herokuapp.com/actors/10  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "actor":
    {
        "age":60,
        "gender":"Nonbinary",
        "id":10,"name":"Big Bird"
    },
    "success":true
}
```

###### GET /movies/id
Returns only the movie whose ID matches the one provided.
- Requires `get:movies` permission.
- Arguments 
  - Movie ID (data-type integer,) at the end of the endpoint.
  - Authorization header bearer token (data-type String.)
- Sample Request:
```
curl -X GET https://castr-capstone-app.herokuapp.com/movies/25  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "movie":
    {
        "id":25,
        "release_date":"Wed, 01 Dec 2021 00:00:00 GMT",
        "title":"Star Wars"
    },
    "success":true
}
```


###### POST /actors
Adds a new actor to the database with details supplied by the end user.
- Requires `post:actors` permission.
- Arguments 
  - Name, data-type String.
  - Age, data-type Integer.
  - Gender, data-type String.
  - Authorization header bearer token is required.
- Sample Request:
```
curl -X POST https://castr-capstone-app.herokuapp.com/actors  -d '{"name":"Gene Wilder", "age":63, "gender":"male"}' -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "actors":
    [
        {"age":60,"gender":"Nonbinary","id":10,"name":"Big Bird"},
        {"age":72,"gender":"female","id":44,"name":"Sigourney Weaver"},
        {"age":55,"gender":"female","id":45,"name":"Halle Berry"},
        {"age":63,"gender":"male","id":46,"name":"Gene Wilder"}
    ],
    "success":true
}
```

###### POST /movies
Adds a new movie to the database with details supplied by the end user.
- Requires `post:movies` permission.
- Arguments 
  - Title, data-type String.
  - Release date, data-type String, formatted as "YYYY-MM-DD".
  - Authorization header bearer token is required.
- Sample Request:
```
curl -X POST https://castr-capstone-app.herokuapp.com/movies -d '{"title":"Avengers", "release_date":"2021-07-08"}' -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "movies":
    [
        {"id":25,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Star Wars"},
        {"id":23,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Jaws"},
        {"id":26,"release_date":"Thu, 08 Jul 2021 00:00:00 GMT","title":"Avengers"}
    ],
    "success":true
}
```

###### PATCH /actors/id
Updates the actor whose ID matches the one provided, with additional arguments supplied by the end user.
- Requires `patch:actors` permission.
- Arguments 
  - Actor ID (data-type integer,) at the end of the endpoint.
  - Name, data-type String.
  - Age, data-type Integer.
  - Gender, data-type String.
  - Authorization header bearer token is required.
- Sample Request:
```
curl -X PATCH https://castr-capstone-app.herokuapp.com/actors/46 -d '{"name":"Gene Wilder", "age":83, "gender":"male"}' -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "actor":
    {
        "age":83,
        "gender":
        "male",
        "id":46,
        "name":"Gene Wilder"
    },
    "success":true
}
```

###### PATCH /movies/id
Updates the movie whose ID matches the one provided, with additional arguments supplied by the end user.
- Requires `patch:movies` permission.
- Arguments 
  - Movie ID (data-type integer,) at the end of the endpoint.
  - Title, data-type String.
  - Release date, data-type String, formatted as "YYYY-MM-DD".
  - Authorization header bearer token is required.
- Sample Request:
```
curl -X PATCH https://castr-capstone-app.herokuapp.com/movies/26 -d '{"title":"Avengers", "release_date":"2012-08-31"}' -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "movie":
    {
        "id":26,
        "release_date":"Fri, 31 Aug 2012 00:00:00 GMT",
        "title":"Avengers"
    },
    "success":true
}

```

###### DELETE /actors/id
Deletes only the actor whose ID matches the one provided.
- Requires `delete:actors` permission.
- Arguments 
  - Actor ID (data-type integer,) at the end of the endpoint.
  - Authorization header bearer token (data-type String.)
- Sample Request:
```
curl -X DELETE https://castr-capstone-app.herokuapp.com/actors/44  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "actors":
    [
        {"age":60,"gender":"Nonbinary","id":10,"name":"Big Bird"},
        {"age":55,"gender":"female","id":45,"name":"Halle Berry"},
        {"age":83,"gender":"male","id":46,"name":"Gene Wilder"}
    ],
    "deleted":44,
    "success":true
}
```

###### DELETE /movies/id
Deletes only the movie whose ID matches the one provided.
- Requires `delete:movies` permission.
- Arguments 
  - Movie ID (data-type integer,) at the end of the endpoint.
  - Authorization header bearer token is required.
- Sample Request:
```
curl -X DELETE https://castr-capstone-app.herokuapp.com/movies/26  -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFzYVJnakZLN0tUVldfWkxkT1RsSCJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AtZnNuZC11ZGFjaXR5LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGRmZDUzZDk2MmNkOTAwNzA1MTliYjgiLCJhdWQiOiJjYXN0ci1hcGkiLCJpYXQiOjE2NDU1OTMyMjksImV4cCI6MTY0NTY3OTYyOSwiYXpwIjoiVjN1ZXZoZld4cmFybFhoeXVRNHIwb0JTVDZpem1ZRjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.B5AACgiUc62M5HcoITOZUmeZvbOwN1vwhsEZaCE3RX8YJ85WJwbcAELW5BuFPldr1sqCF5c8A7OIKukdxMkIk5ZAY3BhieiwzBfzP9LaYikjxOG5Z8Ow3kfMvzgAaSDDFJjIHTYDb56SOEd2z2QZOJtwcgPu5i2RVcKMQovdUfR1evp8uJ5adf1e76F8CGQYarzfgRwU_agfKDld9YWnve35bfp3w8_HBzJYdBk9X1k70VehSf-vyhVdIGxUkn4Y75k-bEpBHFuvqNjDynAb6L9jsyNqGfPByuSthCkeWwTevFALPK9v1NNXSI-7QuYv8GK8ol50SWkLlThY8717Cg"
```
- Sample Response:
```
{
    "deleted":26,
    "movies":
    [
        {"id":25,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Star Wars"},
        {"id":23,"release_date":"Wed, 01 Dec 2021 00:00:00 GMT","title":"Jaws"}
    ],
    "success":true
}
```


## Running Castr Locally
Follow these steps to get this project up and running on your own machine. First open the terminal of your choice and create or navigate to your desired directory. Then clone the project, and open the folder.
```
git init
git clone https://github.com/aliciakott/FSND-udacity-capstone-castr
cd FSND-udacity-capstone-castr
```

#### 1. Installing Dependencies
You will need to download Python, if you don't already have it on your machine. **Please note** that `psycopg2`, one of the core dependencies for this project, *only works up to python version 3.8.* This is very important.

It is recommended that you use a virtual environment to manage the python packages needed for this project, and prevent them from being installed globally which may affect other projects you may wish to run on your machine. To do this in Windows, first install virtualenv. 
```
pip install virtualenv
```
Then create and activate the virtual environment
```
python -m virtualenv env
source env/Scripts/activate
```
Using `ls` you should see `env` listed within your directory. Now you're ready to install the rest of the dependencies.
```
pip install -r requirements.txt
```

#### 2. Setting Up The Database
[Download PostgreSQL](https://www.postgresql.org/download/). When that is finished, open psql which is included with the download, and log in. *Windows users, please note that you may be required to create a password.* If so, keep track of your password, as you will need to add it to the `.env` file shortly. 

Create the database in psql. 
```
create database castr;
```
At this time, you may wish to save yourself a step later and create the database we'll run our test suite against.
```
create database castr_test;
```

- Adjust .env for postgres password, as necessary

#### 3. Managing Migrations
Back in the terminal, begin the data migration. You should already have the Flask-Script and Flask-Migrate packages installed through the `requirements.txt`. Go back into your terminal and enter the following.
```
flask db migrate "Initial migration."
flask db upgrade
```
You should not need to enter the command `flask db init` because this creates the migrations folder and that is already provided. 

#### 4. Run The Server
Because you have the `python-dotenv` package, you need only run the following command in the project folder.
```
python app.py
```
If you're having trouble with this command, try `python3 app.py`. The API should now be served at localhost:5000. This is all you need do to run curl commands against the API and run the test suite. 

#### 5. Serve The Frontend
*Optional* If you wish to run the frontend locally as well, navigate to the `frontend` directory in the terminal and start the Reactjs development server.
```
npm start
```
You should be able to open your browser and see the web app at localhost:3000

## Testing Locally
If you have not already done so, please install dependencies and PostgreSQL as described in steps 1. and 2. of *Running Castr Locally*, then open psql and create the test database.  
```
create database castr_test;
```
Go back into your project root directory and run the server
```
python app.py
```
We need to make some adjustments to our source code before we can run our tests. Open `app.py` in your text editor and look for lines 31 and 32 under the `create_app` function. These should say:
```
# COMMENT OUT setup_db(app) DURING TESTING ONLY!!!
setup_db(app)
```
Comment out `setup_db(app)`. This step will be performed independently of this script by the unittest set up.

Open `models.py` in the database folder. Look for lines 13 and 14 under the `setup_db` function. These should say:
```
# UNCOMMENT OUT db.create_all() DURING TESTING ONLY!!!
# db.create_all()
```
Uncomment `db.create_all`. Our unittest suite will use this in place of Flask-Migrate.

Now we're ready to run our tests
```
python test_castr.py
```