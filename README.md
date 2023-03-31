# modestio
A family project for a cat shelter.

Written in Python with Django. Containerized with Docker.
Potentially convertible into a single-page app in React with RESTful API.

## Stakeholders & Goals

* Business owner

  * get a shelter cat adopted by a family
  * collect donations
  * current expenses
  * specific shelter-wide projects
  * specific animals

* Customer

  * choose and adopt a cat
  * put a stray cat to a shelter
  * donate money or stuff

## Development Policies

* testing: maybe only for selected stories, explicitly planned
* merging: only via code reviews (doesn’t matter who merges)
* language: English

## Development: How To Install [pre-commit](https://pre-commit.com) and its hooks:

```
$ pip install pre-commit
$ pre-commit install
```
Install `tox` and run it:

```
$ tox
```

## Usage

Be sure you have modestio repository copied to your machine.

### Using docker command line

First option is to run both postgres image and Django image as containers manually.

* Run a postgres image as a container first (from project's root directory) using the command:

```
docker run --name modestio-postgres --network modestio-network \
--hostname db --publish 5432:5432 \
--env POSTGRES_PASSWORD=mypassword \
--volume ./postgres_data:/var/lib/postgresql/data \
postgres:latest
```

* Then build the Django image from Dockerfile:

```
docker build -t modestio:2023-03-10 .
```

* And run it as a container:

```
docker run --network modestio-network --publish 8000:8000 \
 --env DATABASE_HOST=db --volume .:/usr/src/app \
modestio:2023-03-10
```

### Using docker-compose file

It's more handy to use a docker-compose file. The only thing you need is to run the command:

```
docker compose up
```
