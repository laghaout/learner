
# Table of Contents

1.  [To-do <code>[1/3]</code>](#org8e0bd11)
2.  [Setup](#org7016217)
3.  [User manual](#orgbab8c3f)
    1.  [Via Docker](#org5f31deb)
        1.  [Single run](#org71311b7)
        2.  [Interactive](#org21d6373)
        3.  [Docker compose](#org87052bd)
    2.  [Via FastAPI](#org61b5869)
    3.  [Via Python import (not tested yet)](#org926e0ae)



<a id="org8e0bd11"></a>

# To-do <code>[1/3]</code>

1.  [ ] `__init__.py` file
2.  [X] Default arguments should be stored as an external JSON or YAML
3.  [ ] Fix `server.py` and `client.py` and integrate them with `main.py` so as to be able to use FastAPI.


<a id="org7016217"></a>

# Setup

1.  [ ] The dataset is to placed by default under `data/`.
2.  [ ] If needed, edit the `config.json`.
3.  [ ] If needed, create a docker image with `docker compose build`.


<a id="orgbab8c3f"></a>

# User manual

Decide which `TASK ∈ {wrangle, train, test, serve}` is to be executed. Not specifying a TASK will run them all in sequence.


<a id="org5f31deb"></a>

## Via Docker


<a id="org71311b7"></a>

### Single run

    docker run -v "$(pwd):/data" learner TASK


<a id="org21d6373"></a>

### Interactive

    docker run -it --entrypoint bash -v "$(pwd):/data" learner


<a id="org87052bd"></a>

### Docker compose

Edit `docker-compose.yml` if needed. The mounted volumes are read-only by default.

    docker compose run learner TASK

For the interactive command line, run this instead:

    docker compose run learner-shell TASK


<a id="org61b5869"></a>

## Via FastAPI

    docker compose run -it -p 8000:8000 --entrypoint uvicorn learner server:app --host 0.0.0.0 --port 8000 --reload


<a id="org926e0ae"></a>

## Via Python import (not tested yet)

    from main import main
    output = main(TASK)

