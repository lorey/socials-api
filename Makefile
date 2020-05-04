.RECIPEPREFIX = >
.PHONY: build chown black isort
.FORCE:

build:
> docker-compose build

requirements.txt: .FORCE
> docker-compose exec web pip freeze > requirements.txt

chown:
> sudo chown -R $$USER ./

black:
> docker-compose exec web black . -l 100

isort:
> docker-compose exec web isort -rc .

precommit: chown isort black requirements.txt