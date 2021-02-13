# DiscuBot

## Setup
* `git clone https://github.com/straend/discu-bot`
* `cd discu-bot`

## Development
### Run services
* start Postgresql at `localhost` with user `postgres` and password `postgres`
* `cd backend`
* Upgrade dev-db `poetry run alembic upgrade head`
* Run Bot `DISCORD_TOKEN=DISCORD_TOKEN poetry run bot.py`
* Run api `poetry run uvicorn main:app --reload`

* Update db config if changing models `poetry run alembic revision --autogenerate`

### Run front
* `cd faster-front`
* `ng serve`

Api docs available at http://localhost:8000/docs
  
Frontend at http://localhost:4200


## "Production"
* `cp example.env .env`
* edit `.env`
* `docker-compose up -d`
