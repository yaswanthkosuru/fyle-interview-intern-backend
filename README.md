
## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
docker compose up

after running above command:

docker build image for flask app ,creates a new volume  ,
everytime we send request via port 7755 flask fetches from volume and returns data. 
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
