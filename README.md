
# Table of Contents

1.  [To-do <code>[1/3]</code>](#org856c8f7)
2.  [Setup](#org8a95e36)
3.  [User manual](#orgb56ba0e)
    1.  [Via Docker](#org0523a0f)
    2.  [Via import](#orgd7f955c)
    3.  [Via FastAPI](#orgdf9864f)



<a id="org856c8f7"></a>

# To-do <code>[1/3]</code>

1.  [ ] `__init__.py` file
2.  [X] Default arguments should be stored as an external JSON or YAML
3.  [ ] Fix `server.py` and `client.py` and integrate them with `main.py` so as to be able to use FastAPI.


<a id="org8a95e36"></a>

# Setup

-   [ ] The dataset is to placed by default under `data/`
-   [ ] Dockerize with `docker compose build`


<a id="orgb56ba0e"></a>

# User manual


<a id="org0523a0f"></a>

## Via Docker

    docker compose run learner $TASK


<a id="orgd7f955c"></a>

## Via import

    import


<a id="orgdf9864f"></a>

## Via FastAPI

    docker run -p 8000:8000 learner

