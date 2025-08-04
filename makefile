demo:
	uv run demo.py

urun:
	uv run uvicorn_main.py

run:
	uv run main.py

freeze:
	uv pip freeze > requirements.txt


docker-build:
	docker compose up --build -d


alembic-revision:
	alembic revision --autogenerate -m "$(m)"


alembic-upgrade:
	alembic upgrade head


secret:
	python src/core/dependencies/auth_dep/secret_generator.py

fs:
	faststream run src.core.tasks.fs.app:app

fs-docs:
	faststream docs serve src.core.tasks.fs.app:app --port 8081
