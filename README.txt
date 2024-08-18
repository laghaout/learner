#+TITLE: Learner pipeline

* To-do [1/3]
1. [ ] =__init__.py= file
2. [X] Default arguments should be stored as an external JSON or YAML
3. [ ] Fix =server.py= and =client.py= and integrate them with =main.py= so as to be able to use FastAPI.
* Setup
- [ ] The dataset is to placed by default under =data/=
- [ ] Dockerize with =docker compose build=
* User manual
** Via Docker

#+BEGIN_SRC bash
docker compose run learner $TASK
#+END_SRC

** Via import

#+BEGIN_SRC python
import
#+END_SRC

** Via FastAPI

#+BEGIN_SRC bash
docker run -p 8000:8000 learner
#+END_SRC


