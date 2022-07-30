# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in
the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for
each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in
the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory
and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle
  requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift
  for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the
  Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for
  encoding, decoding, and verifying JWTS.

## Running the server

From within the `./backend` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

Before running the server, you must also create the database, by uncommenting the `db_drop_and_create_all()` function in
the `src/api.py`
To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

After the server is running, you need to comment out the `db_drop_and_create_all()` function in the `src/api.py` file.

### Test endpoints with [Postman](https://getpostman.com).

The postman collection contains exactly 18 endpoints with the respective test cases.

Before to run the collection, be sure to have at least one drink in the database.

### Stand out from the backend

- `app.py` is the main file for the backend that imports all the other necessary files.
- Add `utils` directory to the `./backend` directory with these files : `./backend/utils/validator.py`
  , `./backend/utils/validator_response.py`,

The `validator.py` file contains functions that validate the data that is sent to the server.
The `validator_response.py` file contains functions that return the appropriate validations errors response to the
client.

- `services` directory contains the `./backend/services/drink_service.py` file to handle the logic for the CRUD actions.

