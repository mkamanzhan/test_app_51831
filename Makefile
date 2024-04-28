VENV := .venv/bin/
LOCAL_APP_URL := http://localhost:8000

help:
	clear
	@echo "================= Usage ================="
	@echo "docker-build     to build the docker image"
	@echo "docker-start     to start the docker containers"
	@echo "docker-restart   to restart the docker containers with build image"
	@echo "docker-stop      to stop the docker containers"
	@echo "docker-test      to run the tests in the docker container"
	@echo "docker-format    to format the code in the docker container"
	@echo "docker-checks    to run the checks in the docker container"
	@echo "start            to start the application"
	@echo "test             to run the tests"
	@echo "format           to format the code"
	@echo "checks           to run the checks"
	@echo "clean            to remove all the temporary files"
	@echo "request-health   to make a request to the health endpoint"

#################
# Docker commands
#################

docker-build:
	docker compose build

docker-start:
	docker compose up -d

docker-restart:
	docker compose down
	docker compose build
	docker compose up -d

docker-stop:
	docker compose down

docker-test:
	docker compose run --rm app make test

docker-format:
	docker compose run --rm app make format

docker-checks:
	docker compose run --rm app make checks

################
# Local commands
################

start:
	$(VENV)python main.py

test:
	$(VENV)pytest tests

format:
	$(VENV)black src tests main.py
	$(VENV)isort src tests main.py
	$(VENV)ruff check --fix src tests main.py
	echo "All formatting done!"

checks:
	$(VENV)bandit -r src
	$(VENV)isort src tests main.py --check
	$(VENV)black src tests main.py --check
	$(VENV)mypy src tests main.py
	$(VENV)ruff check src tests main.py
	echo "All checks passed!"


clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

################
# Request commands
################

request-health:
	curl -s -X GET $(LOCAL_APP_URL)/health | pdm run python -m json.tool
