.RECIPEPREFIX = >
.PHONY: build chown
.FORCE:

build:
> docker-compose build

requirements.txt: .FORCE
> docker-compose exec web pip freeze > requirements.txt

chown:
> sudo chown -R $$USER ./
