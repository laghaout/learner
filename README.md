
# Table of Contents

1.  [To-do <code>[1/3]</code>](#orgd1381ce)
2.  [Setup](#orgc56dbc5)
3.  [User manual](#org2fc815d)
    1.  [Via Docker](#orgfa73dfb)
        1.  [Single run](#orgb08076e)
        2.  [Interactive](#orgf40e5af)
        3.  [Docker compose](#orgb66ea8b)
    2.  [Via FastAPI](#org4eaad0c)
    3.  [Via Python import (not tested yet)](#org1b9cbc5)



<a id="orgd1381ce"></a>

# To-do <code>[1/3]</code>

1.  [ ] `__init__.py` file
2.  [X] Default arguments should be stored as an external JSON or YAML
3.  [ ] Fix `server.py` and `client.py` and integrate them with `main.py` so as to be able to use FastAPI.


<a id="orgc56dbc5"></a>

# Setup

1.  [ ] The dataset is to placed by default under `data/`.
2.  [ ] If needed, edit the `config.json`.
3.  [ ] If needed, create a docker image with `docker compose build`.


<a id="org2fc815d"></a>

# User manual

Decide which `TASK ∈ {wrangle, train, test, serve}` is to be executed. Not specifying a TASK will run them all in sequence.


<a id="orgfa73dfb"></a>

## Via Docker


<a id="orgb08076e"></a>

### Single run

    docker run -v "$(pwd):/data" learner TASK


<a id="orgf40e5af"></a>

### Interactive

    docker run -it --entrypoint bash -v "$(pwd):/data" learner


<a id="orgb66ea8b"></a>

### Docker compose

Edit `docker-compose.yml` if needed. The mounted volumes are read-only by default.

    docker compose run learner TASK

For the interactive command line, run this instead:

    docker compose run learner-shell


<a id="org4eaad0c"></a>

## Via FastAPI

    docker compose run -it -p 8000:8000 --entrypoint uvicorn learner server:app --host 0.0.0.0 --port 8000 --reload


<a id="org1b9cbc5"></a>

## Via Python import (not tested yet)

    from main import main
    output = main(TASK)

