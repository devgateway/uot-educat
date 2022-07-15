#!/bin/bash

COMPOSE_ENV_FILE=.env.prod

# pull new changes from remote
git pull

# update the app
./up.sh
