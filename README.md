
# Table of Contents

1.  [To-do <code>[1/3]</code>](#org58ea0e9)
2.  [Setup](#org1e76fa5)
3.  [User manual](#orgbe604a1)
    1.  [Via Docker](#orgb24caea)
        1.  [Single run](#orgc3500d4)
        2.  [Interactive](#org9ad7adb)
        3.  [Docker compose](#orga34992f)
    2.  [Via FastAPI](#orgdcf54b1)
    3.  [Via Python import (not tested yet)](#orgbda1535)



<a id="org58ea0e9"></a>

# To-do <code>[1/3]</code>

1.  [ ] `__init__.py` file
2.  [X] Default arguments should be stored as an external JSON or YAML
3.  [ ] Fix `server.py` and `client.py` and integrate them with `main.py` so as to be able to use FastAPI.


<a id="org1e76fa5"></a>

# Setup

1.  [ ] The dataset is to placed by default under `data/`.
2.  [ ] If needed, edit the `config.json`.
3.  [ ] If needed, create a docker image with `docker compose build`.


<a id="orgbe604a1"></a>

# User manual

Decide which `TASK ∈ {wrangle, train, test, serve}` is to be executed. Not specifying a TASK will run them all in sequence.


<a id="orgb24caea"></a>

## Via Docker


<a id="orgc3500d4"></a>

### Single run

    docker run -v "$(pwd):/data" learner TASK


<a id="org9ad7adb"></a>

### Interactive

    docker run -it --entrypoint bash -v "$(pwd):/data" learner


<a id="orga34992f"></a>

### Docker compose

Edit `docker-compose.yml` if needed. The mounted volumes are read-only by default.

    docker compose run learner TASK

For the interactive command line, run this instead:

    docker compose run learner-shell TASK


<a id="orgdcf54b1"></a>

## Via FastAPI

    docker compose run -it -p 8000:8000 --entrypoint uvicorn learner server:app --host 0.0.0.0 --port 8000 --reload


<a id="orgbda1535"></a>

## Via Python import (not tested yet)

    from main import main
    output = main(TASK)

