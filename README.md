# fastapi_sample

This project was generated using fastapi_template.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m fastapi_sample
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Local dev:
After start docker, you can manual start `api` by run file `fastapi_sample\__main__.py`

## Create Project Option
```shell
python -m fastapi_template
```
```shell
API type
> REST API
  GrapQL API
```
```shell
Database
  No database
  SQLite database
  MySQL database
> PostgreSQL database
├── Description ──────────────────────────────────────────────────────────────────
| PostgreSQL is second most popular open-source ralational database.
| It's a good fit for production-grade application
├────────────────────────────────────────────────────────────────────
```
```shell
ORM
  Whithout ORMs
  Ormar
> SQLAlchemy
  Tortoise
  PsycoPG
  Piccolo
├── Description ──────────────────────────────────────────────────────────────────
| SQLAlchemy is the most popular python ORM.
| It ha a great documentation and a big community around it.
├────────────────────────────────────────────────────────────────────
```
```shell
CI|CD
  Do not add CI/CD
  Gitlab CI
  Github Action
├── Description ──────────────────────────────────────────────────────────────────
| Use this option if you use gitlab as your VCS.
| This option will add test job in your `.gitlab-ci.yml` file.
| (To use it please use docker or kubernetes executors).
├────────────────────────────────────────────────────────────────────
```
```shell
Additional tweaks
[ ] Use older version of pydantic
[*] Add redis support
[ ] Add fastapi-users support
[ ] Add RabbitMQ support
[ ] Add Taskiq support
[ ] Add Migrations
[ ] Add kubernetes config
[*] Add dummy model
[*] Add example router
[*] Add self hosted swagger
[*] Add prometheus compatible metrics
[*] Add sentry integration
[ ] Add loguru logger
[ ] Add opentelemetry integration
[ ] Add traefik labels to docker container
[ ] Add Kafka support
[*] Add gunicorn server
├── Description ──────────────────────────────────────────────────────────────────
| This option adds gunicorn server for running application.
| It's more performant than uvicorn, and recommended for production
├────────────────────────────────────────────────────────────────────
```

## Project structure
```bash
$ tree "fastapi_sample"
fastapi_sample
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "FASTAPI_SAMPLE_" prefix.

For example if you see in your "fastapi_sample/settings.py" a variable named like
`random_parameter`, you should provide the "FASTAPI_SAMPLE_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `fastapi_sample.settings.Settings.Config`.

An example of .env file:
```bash
FASTAPI_SAMPLE_RELOAD="True"
FASTAPI_SAMPLE_PORT="8000"
FASTAPI_SAMPLE_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);

Run this cmd to check before commit:
```shell
pre-commit run --all-files
```


You can read more about pre-commit here: https://pre-commit.com/


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=fastapi_sample" -e "POSTGRES_USER=fastapi_sample" -e "POSTGRES_DB=fastapi_sample" postgres:13.8-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```
