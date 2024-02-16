# Albums API

Small service containing information about music albums

## Headers

**Authorization**: `Bearer <access_token>` for all albums endpoints


## Endpoints

All endpoints require Authorization except `/auth/login`

### POST `/auth/login`
- Returns a JWT token for authenticating with the API.
- Provide credentials through Basic Authentication
- **Responses**
    - 200: Authentication successful, returns JWT token
    - 401: Authentication failed 

### GET `/albums/`
- Retrieves all albums.
- **Responses**:
  - 200: Success, returns a list of albums.
  - 401: Unauthorized.

### POST `/albums/`
- Creates a new album.
- **Example Body**: `{"title": "Album Title", "artist": "Artist Name", "release_year": 2021, "genre": "Rock"}`
- **Responses**:
  - 201: Created, returns the created album.
  - 400: Bad Request, if data is invalid.
  - 401: Unauthorized.

### GET `/albums/<id>`
- Retrieves a specific album by ID.
- **Responses**:
  - 200: Success, returns the specified album.
  - 404: Not Found, if the album does not exist.
  - 401: Unauthorized.

### DELETE `/albums/<id>`
- Deletes a specific album by ID.
- **Responses**:
  - 204: No Content. Returned whether resource was deleted or not.
  - 401: Unauthorized.

### PUT `/albums/<id>`
- Updates a specific album by ID.
- **Body**: JSON object containing the fields to update.
- **Responses**:
  - 200: Success, returns the updated album.
  - 404: Not Found, if the album does not exist.



## Local environment

To run locally, you need to create a `.env` file in the root of the project with at least the following values

```bash
MARIADB_USER=<db_user>
MARIADB_PASSWORD=<db_psswd>
MARIADB_DATABASE=<db_name>

SECRET_KEY=<secret_key>
```
### Utilities

#### Load Album data

To make testing the API easier, you can download this [dataset](https://www.kaggle.com/datasets/joebeachcapital/rolling-stones-500-greatest-albums-of-all-time) from Kaggle. 

To load it into the database, just run the utility script and give the CSV as the first parameter `./load_initial_data.sh /path/to/csv`

#### Create user

To create a user for the api, run the following command in the project root

```docker compose exec -i api flask cli create-user```

## Jenkins

My previous experience is only using Gitlab CI tooling, so the `Jenkinsfile` is quite bare. To get it running, I created a multibranch pipeline in Jenkins that is tied to this Github repository. 

Only thing the pipeline currently does is build a test image and then runs linting using `flake8`

## Notes

- Thi