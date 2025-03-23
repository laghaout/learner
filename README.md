
# Table of Contents

1.  [To-do <code>[1/3]</code>](#orgbfa7696)
2.  [Setup](#org8efd97b)
3.  [User manual](#org2c41f63)
    1.  [Via Docker](#org0bdfbfb)
        1.  [Single run](#org7b2e940)
        2.  [Interactive](#org3526770)
        3.  [Docker compose](#org465eece)
    2.  [Via FastAPI](#org8bb9bc9)
    3.  [Via Python import (not tested yet)](#orgd01ce6c)



<a id="orgbfa7696"></a>

# To-do <code>[1/3]</code>

1.  [ ] `__init__.py` file
2.  [X] Default arguments should be stored as an external JSON or YAML
3.  [ ] Fix `server.py` and `client.py` and integrate them with `main.py` so as to be able to use FastAPI.


<a id="org8efd97b"></a>

# Setup

1.  [ ] The dataset is to placed by default under `data/`.
2.  [ ] If needed, edit the `config.json`.
3.  [ ] If needed, create a docker image with `docker compose build`.


<a id="org2c41f63"></a>

# User manual

Decide which `TASK ∈ {wrangle, train, test, serve}` is to be executed. Not specifying a TASK will run them all in sequence.


<a id="org0bdfbfb"></a>

## Via Docker


<a id="org7b2e940"></a>

### Single run

    docker run -v "$(pwd):/learner" learner TASK


<a id="org3526770"></a>

### Interactive

    docker run -it --entrypoint bash -v "$(pwd):/learner" learner


<a id="org465eece"></a>

### Docker compose

Edit `docker-compose.yml` if needed.

    docker compose run learner TASK

For the interactive command line, run this instead:

    docker compose run learner-shell


<a id="org8bb9bc9"></a>

## Via FastAPI

    docker compose run -it -p 8000:8000 --entrypoint uvicorn learner server:app --host 0.0.0.0 --port 8000 --reload


<a id="orgd01ce6c"></a>

## Via Python import (not tested yet)

    from main import main
    output = main(TASK)

