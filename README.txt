#+TITLE: Learner pipeline

* To-do [1/3]
1. [ ] =__init__.py= file
2. [X] Default arguments should be stored as an external JSON or YAML
3. [ ] Fix =server.py= and =client.py= and integrate them with =main.py= so as to be able to use FastAPI.
* Setup
1. [ ] The dataset is to placed by default under =data/=.
2. [ ] If needed, edit the =config.json=.
3. [ ] If needed, create a docker image with =docker compose build=.
* User manual
Decide which =TASK ∈ {wrangle, train, test, serve}= is to be executed. Not specifying a TASK will run them all in sequence.
** Via Docker
*** Single run
#+BEGIN_SRC bash
docker run -v "$(pwd):/data" learner TASK
#+END_SRC
*** Interactive
#+BEGIN_SRC bash
docker run -it --entrypoint bash -v "$(pwd):/data" learner
#+END_SRC
*** Docker compose
Edit =docker-compose.yml= if needed. The mounted volumes are read-only by default.
#+BEGIN_SRC bash
docker compose run learner TASK
#+END_SRC
For the interactive command line, run this instead:
#+BEGIN_SRC bash
docker compose run learner-shell
#+END_SRC
** Via FastAPI
#+BEGIN_SRC bash
docker compose run -it -p 8000:8000 --entrypoint uvicorn learner server:app --host 0.0.0.0 --port 8000 --reload
#+END_SRC
** Via Python import (not tested yet)
#+BEGIN_SRC python
from main import main
output = main(TASK)
#+END_SRC
