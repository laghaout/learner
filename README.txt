#+TITLE: Learner pipeline

* To-do [/]
1. [ ] =__init__.py= file
2. [ ] Default arguments should be stored as an external JSON or YAML.
* User manual
1. Place the dataset =DK-DK2.csv= under =data/=
2. Dockerize with =docker compose build=
3. Run the training with =docker compose run forecast train= or the serving with =docker compose run forecast serve=

docker run -p 8000:8000 learner
